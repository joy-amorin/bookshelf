import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import BookList from './BookList';
import BookDetails from './BookDetails';
import AddBook from './AddBook';

function App() {
    return (
        <Router>
            <div>
                <Routes>
                    <Route path="/" element={<BookList />} />
                    <Route path="/books/:id" element={<BookDetails />} />
                    <Route path="/add" element={<AddBook />} />
                </Routes>
            </div>
        </Router>
    );
}

export default App;
