from dataclasses import dataclass, field
from typing import List, Set
import re
import datetime

@dataclass
class Note:
    id: int
    title: str
    content: str
    tags: List[str] = field(default_factory=list)
    created_at: str = field(default_factory=lambda: datetime.datetime.now(datetime.timezone.utc).isoformat())

    @staticmethod
    def extract_tags(text: str) -> List[str]:
        # Extract hashtags like #react #python
        return sorted(list(set(re.findall(r"#([a-zA-Z0-9_\-]+)", text))))

class NoteRepository:
    def __init__(self):
        self._notes = {}
        self._counter = 1

    def create(self, title: str, content: str) -> Note:
        tags = Note.extract_tags(content)
        note = Note(id=self._counter, title=title, content=content, tags=tags)
        self._notes[self._counter] = note
        self._counter += 1
        return note

    def get(self, note_id: int):
        return self._notes.get(note_id)

    def search(self, query: str = None, tag: str = None) -> List[Note]:
        results = list(self._notes.values())
        if tag:
            results = [n for n in results if tag.lower() in [t.lower() for t in n.tags]]
        if query:
            q = query.lower()
            results = [n for n in results if q in n.title.lower() or q in n.content.lower()]
        return results

    def delete(self, note_id: int) -> bool:
        if note_id in self._notes:
            del self._notes[note_id]
            return True
        return False
