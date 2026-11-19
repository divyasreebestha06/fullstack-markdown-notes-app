import React, { useState } from 'react';

export function MarkdownNotes({ initialNotes = [] }) {
  const [notes, setNotes] = useState(initialNotes);
  const [filterTag, setFilterTag] = useState('');
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');

  const handleAddNote = () => {
    if (!title.trim() || !content.trim()) return;
    const extractedTags = (content.match(/#([a-zA-Z0-9_\-]+)/g) || []).map(t => t.slice(1));
    const newNote = {
      id: Date.now(),
      title,
      content,
      tags: extractedTags,
      created_at: new Date().toISOString()
    };
    setNotes([newNote, ...notes]);
    setTitle('');
    setContent('');
  };

  const filteredNotes = filterTag
    ? notes.filter(n => n.tags.includes(filterTag))
    : notes;

  return (
    <div className="markdown-notes-container" style={{ padding: 20, fontFamily: 'sans-serif' }}>
      <h2>📝 Markdown Knowledge Base</h2>
      <div style={{ marginBottom: 16 }}>
        <input
          placeholder="Note title"
          value={title}
          onChange={e => setTitle(e.target.value)}
          style={{ marginRight: 8, padding: 6 }}
        />
        <textarea
          placeholder="Note content with #tags (e.g. Learning #fastapi and #react)"
          value={content}
          onChange={e => setContent(e.target.value)}
          rows={3}
          style={{ width: '100%', marginTop: 8, padding: 6 }}
        />
        <button onClick={handleAddNote} style={{ marginTop: 8, padding: '6px 16px' }}>Save Note</button>
      </div>
      <div>
        <h3>All Notes ({filteredNotes.length})</h3>
        {filteredNotes.map(n => (
          <div key={n.id} style={{ border: '1px solid #ddd', padding: 12, marginBottom: 8, borderRadius: 4 }}>
            <h4>{n.title}</h4>
            <p>{n.content}</p>
            <div>
              {n.tags.map(t => (
                <span key={t} onClick={() => setFilterTag(t)} style={{ background: '#e0f2fe', color: '#0369a1', padding: '2px 8px', borderRadius: 12, marginRight: 6, cursor: 'pointer', fontSize: 12 }}>
                  #{t}
                </span>
              ))}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
