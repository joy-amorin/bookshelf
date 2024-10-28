import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import BookList from './BookList';
import BookDetails from './BookDetails';
import AddBook from './AddBook';
import ReadingPlan from './ReadingPlan';
import ReadingPlanView from './ReadingPlanView';


function App() {
    return (
        <Router>
            <div>
                <Routes>
                    <Route path="/" element={<BookList />} />
                    <Route path="/books/:id" element={<BookDetails />} />
                    <Route path="/add" element={<AddBook />} />
                    <Route path="/reading-plan/:bookId" element={<ReadingPlan />} />
                    <Route path="/reading-plan-view" element={<ReadingPlanView />} />

                </Routes>
            </div>
        </Router>
    );
}

export default App;
