import React, { useState } from 'react';
import { Link, useParams, useNavigate } from "react-router-dom";
import axios from 'axios';

const ReadingPlan = () => {
    const { bookId } = useParams(); 
    const [pages, setPages] = useState('');
    const [days, setDays] = useState('');
    const [message, setMessage] = useState('');
    const [dayList, setDayList] = useState([]); // estado para la lista de días
    const [completeDay, setCompleteDay] = useState([]); // estado para los días completados
    const [planId, setPlainId] = useState(null); // Estado para el id del plan de lectura
    const navigate = useNavigate(); // hook para navegación

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            const response = await axios.post('http://localhost:8000/reading-plans/add/', {
                pages: parseInt(pages),
                days: parseInt(days),
                book: bookId,
            });
            setPlainId(response.data.id);
            setMessage(`Plan de lectura: ${response.data.pages_per_day} páginas por día`);

            // Generar la lista de días
            const totalDays = parseInt(days);
            const daysArray = Array.from({ length: totalDays }, (_, i) => i + 1);
            setDayList(daysArray); // guardar la lista de días

        } catch (error) {
            setMessage(`Error: ${error.response?.data?.detail || error.message}`);
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

            {message && dayList.length > 0 && ( // Mostrar el botón solo si hay mensaje y días
                <button onClick={() => navigate('/reading-plan-view', { state: { dayList, completeDay: [], planId } })}>
                    Ver Plan
                </button>
            )}
        </div>
    );
};

export default ReadingPlan;
