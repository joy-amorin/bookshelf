import React, { useState } from 'react';
import { Link, useParams } from "react-router-dom";
import axios from 'axios'
import Calendar from "react-calendar";

const ReadingPlan = () => {
    const {bookId} = useParams(); 
    const [pages, setPages] = useState('');
    const [days, setDays] = useState('');
    const [message, setMessage] = useState('');
    const [completedDays, setCompletedDays] = useState([]); // Días completados
    const [selectedDate, setSelectedDate] = useState(new Date()); // Fecha seleccionada en el calendario


    const handleSubmit = async (e) => {
    e.preventDefault();

    try {
        const response = await axios.post('http://localhost:8000/reading-plans/add/', {
            pages: parseInt(pages),
            days: parseInt(days),
            book: bookId,
        });
        setMessage(`Plan de lectura: ${response.data.pages_per_day} páginas por día`)
    }catch (error) {
        setMessage(`Error: ${error.response.data.detail || error.message}`)
    }
    };
    const handleDayClick = (date) => {
        if (!completedDays.includes(date.toDateString())) {
            setCompletedDays([...completedDays, date.toDateString()])
        }
    };

    return (
        <div className="form-container">
            <form onSubmit={handleSubmit}>
                <input
                    type="number"
                    placeholder="Cantidad de páginas"
                    value={pages}
                    onChange={(e) => setPages(e.target.value)}
                    required
                />
                <input
                    type="number"
                    placeholder="Días de lectura"
                    value={days}
                    onChange={(e) => setDays(e.target.value)}
                    required
                />
                <button type="submit">Crear plan de Lectura</button>
            </form>
            {message && <p>{message}</p>}

            {/* Calendar */}
            <Calendar
                onClickDay={handleDayClick}
                value={selectedDate}
            />
            {/*Show completed days}*/}
            <div>
            <h3>Días Completados:</h3>
                <ul>
                    {completedDays.map((day, index) => (
                        <li key={index}>{day}</li>
                    ))}
                </ul>
            </div>
        </div>
    );
};
export default ReadingPlan;
