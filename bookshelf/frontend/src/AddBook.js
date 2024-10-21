import React, { useState } from "react";
import { Link } from "react-router-dom";
import './style/AddBook.css'

const AddBook = () => {
    const [title, setTitle] = useState('');
    const [author, setAuthor] = useState('');
    const [genre, setGenre] = useState('');
    const [sucessMessage, setSucessMessage] = useState('')

    const handleSubmit = async (e) => {
        e.preventDefault();

        const bookData = {
            title: title,
            author: {
                author: author
            },
            genre: {
                genre: genre
            }
        };

        try {
            const response = await fetch('http://127.0.0.1:8000/api/books/add/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(bookData)
            });

            if (response.ok) {
                const data = await response.json();
                console.log('Libro agregado:', data);
                setSucessMessage(`El libro "${data.title}" fue agregado conéxito`)
                setTitle('');
                setAuthor('');
                setGenre('');
            } else {
                const errorData = await response.json();
                setSucessMessage(`Error: ${errorData.error || 'No se puede agregar libro'}`);
                console.error('Error al agregar libro:', errorData);
                setTitle('');
                setAuthor('');
                setGenre('');
            }
        } catch (error) {
            setSucessMessage('Error en la solicitud. Inténtalo de nuevo.');
            console.error('Error en la solicitud', error);
        }
    };

    return (
        <div className="form-container">
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    placeholder="título del libro"
                    value={title}
                    onChange={(e) => setTitle(e.target.value)}
                    required
                />
                <input
                    type="text"
                    placeholder="autor"
                    value={author}
                    onChange={(e) => setAuthor(e.target.value)}
                    required
                />
                <input
                    type="text"
                    placeholder="género"
                    value={genre}
                    onChange={(e) => setGenre(e.target.value)}
                    required
                />
                <button type="submit">Agregar Libro</button>
            </form>
            <div className="animation-container"></div>
            {sucessMessage && <p>{sucessMessage}</p>}
            <Link to="/" className="book-list-link-2">
                Ir a la lista de libros <i className="fas fa-book"></i> 
            </Link>
        </div>
    );
};

export default AddBook;
