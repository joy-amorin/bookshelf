import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom'
import './style/BookList.css'

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

  const handleDelete = async (id) => {
    const confirmDelete = window.confirm("Estás seguro/a que quieres eliminar este libro?")
    if (confirmDelete) {
      const response = await fetch(`http://127.0.0.1:8000/api/books/delete/${id}/`, {
        method: 'DELETE',
      });
      if(response.ok) {
        //update list's book after delete
        setBooks(books.filter(book => book.id !== id));
        console.log("Libro eliminado correctamente");
      } else {
        console.error("Error al eliminar Libro")
      }
    }
  }

  return (
    <div className='book-list-conatiner'>
      <h1 className='book-list-title'>Mi Biblioteca</h1>
      <ul className='book-list'>
        {books.map((book) => (
          <li key={book.id} className='book-list-item'>
            <div className='book-item-container'>
              <Link to={`/books/${book.id}`} className='book-list-link'>{book.title}</Link>
              <button onClick={()=> handleDelete(book.id)} className='book-list-button'>Eliminar</button>
            </div>
          </li>  
        ))}
      </ul>
      <Link to="/add">Agregar Libro</Link>
    </div>
  );
};

export default BookList;