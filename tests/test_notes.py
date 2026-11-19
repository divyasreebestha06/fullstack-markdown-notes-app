import unittest
from backend.models import NoteRepository, Note

class TestMarkdownNotes(unittest.TestCase):
    def setUp(self):
        self.repo = NoteRepository()

    def test_hashtag_extraction(self):
        text = "Studying #algorithms and #data-structures for #interviews! #algorithms"
        tags = Note.extract_tags(text)
        self.assertEqual(tags, ["algorithms", "data-structures", "interviews"])

    def test_create_and_search_by_tag(self):
        n1 = self.repo.create("FastAPI Setup", "Setup guide for #python #fastapi")
        n2 = self.repo.create("React Hooks", "Guide for #react and #frontend")
        
        py_notes = self.repo.search(tag="python")
        self.assertEqual(len(py_notes), 1)
        self.assertEqual(py_notes[0].id, n1.id)

        react_notes = self.repo.search(tag="react")
        self.assertEqual(len(react_notes), 1)
        self.assertEqual(react_notes[0].id, n2.id)

    def test_search_by_text(self):
        self.repo.create("Docker Guide", "Containerize fullstack applications")
        res = self.repo.search(query="Containerize")
        self.assertEqual(len(res), 1)

    def test_delete_note(self):
        n = self.repo.create("Temp", "Temporary #scratch")
        self.assertTrue(self.repo.delete(n.id))
        self.assertFalse(self.repo.delete(999))

if __name__ == "__main__":
    unittest.main()
