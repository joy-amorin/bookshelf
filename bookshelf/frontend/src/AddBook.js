import React, { useState } from "react";

const AddBook = () => {
    const [title, setTitle] = useState('');
    const [author, setAuthor] = useState('');
    const [genre, setGenre] = useState('');

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
            } else {
                const errorData = await response.json();
                console.error('Error al agregar libro:', errorData);
            }
        } catch (error) {
            console.error('Error en la solicitud', error);
        }
    };

    return (
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
    );
};

export default AddBook;
