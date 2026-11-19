from backend.models import NoteRepository

repo = NoteRepository()

def api_create_note(data: dict):
    title = data.get("title")
    content = data.get("content")
    if not title or not content:
        return {"error": "Missing title or content"}, 400
    note = repo.create(title, content)
    return note.__dict__, 201

def api_list_notes(query: str = None, tag: str = None):
    notes = repo.search(query=query, tag=tag)
    return [n.__dict__ for n in notes], 200

def api_delete_note(note_id: int):
    success = repo.delete(note_id)
    if not success:
        return {"error": "Note not found"}, 404
    return {"message": "Note deleted"}, 200
