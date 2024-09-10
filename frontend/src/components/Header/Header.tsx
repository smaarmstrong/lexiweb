import React, { useState } from 'react';
import axios from 'axios';

const Header: React.FC = () => {
  const [searchTerm, setSearchTerm] = useState('');
  const [newTextTitle, setNewTextTitle] = useState('');

  const handleSearch = async (e: React.FormEvent) => {
    e.preventDefault();
    // Implement search functionality
    console.log('Searching for:', searchTerm);
    // You'll need to implement the API call to search for texts
  };

  const handleCreateText = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const response = await axios.post('/api/texts/', {
        title: newTextTitle,
        content: '',
      });
      console.log('Created new text:', response.data);
      setNewTextTitle('');
      // You might want to update the UI or redirect to the new text's page
    } catch (error) {
      console.error('Error creating text:', error);
    }
  };

  return (
    <header className="header">
      <nav>
        <ul>
          <li>
            <a href="/">Home</a>
          </li>
          <li>
            <a href="/texts">Browse Texts</a>
          </li>
          <li>
            <a href="/stats">Stats</a>
          </li>
        </ul>
      </nav>
      <form onSubmit={handleSearch}>
        <input
          type="text"
          placeholder="Search texts..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
        />
        <button type="submit">Search</button>
      </form>
      <form onSubmit={handleCreateText}>
        <input
          type="text"
          placeholder="New text title..."
          value={newTextTitle}
          onChange={(e) => setNewTextTitle(e.target.value)}
        />
        <button type="submit">Add Text</button>
      </form>
    </header>
  );
};

export default Header;
