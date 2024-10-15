import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

const BookDetails = () => {
    const [book, setBook] = useState(null); // Inicializes the book status
    const { id: bookId } = useParams(); // Use useParams to get the ID book

    useEffect(() => {
        const fetchBook = async () => {
            try {
                const response = await fetch(`http://127.0.0.1:8000/api/books/${bookId}/`);
                if(!response.ok) {
                    throw new Error(`Errpr ${response.status} ${response.statusText}`);
                }
                const data = await response.json();
                setBook(data);
            } catch (error) {
                console.error('Error fetching book details', error);
            }
        };
        fetchBook();
    }, [bookId]);

    if (!book) return <div>Loading...</div>;

    return (
        <div>
            <h1>{book.title}</h1>
            <p>Autor: {book.author.author}</p>
            <p>Género: {book.genre.genre}</p>
        </div>
    );
};

export default BookDetails;
