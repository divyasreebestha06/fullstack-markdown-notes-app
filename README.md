# 📝 fullstack-markdown-notes-app

[![React](https://img.shields.io/badge/React-18-61DAFB?style=for-the-badge&logo=react&logoColor=black)](frontend/)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](backend/)
[![CI](https://img.shields.io/badge/Build-Passing-brightgreen?style=for-the-badge)](ci/)

Full-Stack Markdown Knowledge Base with real-time tag indexing, full-text search, and RESTful API.

## Features
- **Automatic Hashtag Parsing:** Extracts `#tag` markers dynamically from markdown content.
- **Fast Tag & Text Filtering:** In-memory inverted index query execution.
- **React Frontend:** Reactive note cards and instant client-side tag filtering.
- **RESTful Endpoints:** Complete API for note creation, retrieval, and deletion.

## Running Tests
```bash
python -m unittest tests/test_notes.py
```
