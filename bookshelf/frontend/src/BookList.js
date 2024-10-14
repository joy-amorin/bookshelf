import React, { useEffect, useState } from 'react';

const BookList = () => {
  const [books, setBooks] = useState([]);

  useEffect(() => {
    // Fetch the list of books from the API
    const fetchBooks = async () => {
      try {
        const response = await fetch('http://127.0.0.1:8000/api/books/');
        const data = await response.json();
        setBooks(data);
      } catch (error) {
        console.error('Error fetching books:', error);
      }
    };

    fetchBooks();
  }, []);

  return (
    <div>
      <h1>Lista de Libros</h1>
      <ul>
        {books.map((book) => (
          <li key={book.id}>{book.title} - {book.author.author}</li>
        ))}
      </ul>
    </div>
  );
};

export default BookList;
