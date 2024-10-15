import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom'

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
          <li key={book.id}>
            <Link to={`/books/${book.id}`}>{book.title}</Link>
          </li>  
        ))}
      </ul>
      <Link to="/add">Agregar Libro</Link>
    </div>
  );
};

export default BookList;