import React, { useState } from 'react';
import { useLocation } from 'react-router-dom';

const ReadingPlanView = () => {
    const location = useLocation();
    const { dayList, completeDay } = location.state || { dayList: [], completeDay: [] };
    
    // Estado local para manejar los días completados
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
        </div>
    );
};

export default ReadingPlanView;
