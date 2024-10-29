import React, { useState } from 'react';
import { useLocation } from 'react-router-dom';
import axios from 'axios';

const ReadingPlanView = () => {
    const location = useLocation();
    const { dayList, completeDay, planId } = location.state || { dayList: [], completeDay: [], planId: null };

    
    // Local status to manage the completed days
    const [completedDays, setCompletedDays] = useState(completeDay);

    const toggleDayCompletion = (day) => {
        setCompletedDays((prevCompletedDays) => {
            if (prevCompletedDays.includes(day)) {
                return prevCompletedDays.filter((completeDay) => completeDay !== day);    
            } else {
                return [...prevCompletedDays, day];
            }
        });
    };

    //Method to save the progress
    const SaveProgress = async () => {
        try {
            await axios.patch(`http://localhost:8000/reading-plans/update-progress/${planId}/`, {
                completed_days: completedDays
            });
            alert('Progreso guardado')
        } catch(error) {
            alert(`Error al guardar el progreso: ${error.response?.data?.detail || error.message}`)
        }
    };


    return (
        <div>
            <h2>Tu Plan de Lectura</h2>
            <ul>
                {dayList.map((day) => (
                    <li key={day}>
                        <label>
                            <input 
                                type="checkbox" 
                                checked={completedDays.includes(day)} 
                                onChange={() => toggleDayCompletion(day)}
                            />
                            Día {day}
                        </label>
                    </li>
                ))}
            </ul>
            <button onClick={SaveProgress}>Guardar Progreso</button>
        </div>
    );
};

export default ReadingPlanView;
