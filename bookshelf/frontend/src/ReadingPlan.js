import React, { useState } from 'react';
import { Link, useParams } from "react-router-dom";
import axios from 'axios';

const ReadingPlan = () => {
    const {bookId} = useParams(); 
    const [pages, setPages] = useState('');
    const [days, setDays] = useState('');
    const [message, setMessage] = useState('');
    const [dayList, setDayList] = useState([]); // status for the day list
    const [completeDay, setCompleteDay] = useState([]); // status for the complete days


    const handleSubmit = async (e) => {
    e.preventDefault();

    try {
        const response = await axios.post('http://localhost:8000/reading-plans/add/', {
            pages: parseInt(pages),
            days: parseInt(days),
            book: bookId,
        });
        setMessage(`Plan de lectura: ${response.data.pages_per_day} páginas por día`)

        // generate days list
        const totalDays = parseInt(days)
        const daysArray = Array.from({ length: totalDays}, (_, i)=> i + 1);
        setDayList(daysArray) //save the days list

    }catch (error) {
        setMessage(`Error: ${error.response.data.detail || error.message}`)
    }
    };
    const toggleDayCompletion = (day) => {
        setCompleteDay((prevCompleteDays) => {
            if (prevCompleteDays.includes(day)) {
                return prevCompleteDays.filter((completeDay) => completeDay !== day );    
            } else {
                return [...prevCompleteDays, day]
            }
        });
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

            <ul>
                {dayList.map((day) => (
                    <li key={day}>
                        <label>
                            <input 
                                type="checkbox"
                                checked={completeDay.includes(day)}
                                onChange={() => toggleDayCompletion(day)}
                            />
                            Día {day}
                        </label>
                    </li>
                ))}
            </ul>
        </div>
    );
};
export default ReadingPlan;
