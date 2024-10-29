import React, { useEffect, useState} from "react";
import axios from "axios";

const ReadingPlanList = () => {
    const [plans, setPlans] = useState([]);
    const [loading, SetLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchPlans = async () => {
            try {
                const response = await axios.get('http://localhost:8000/reading-plans/')
                setPlans(response.data)
            }
            catch (err) {
                setError('Error al cargar los planes de lectura')
            } finally {
                SetLoading(false)
            }
        };
        fetchPlans();
    }, [])

    if (loading) return <p>Cargando planes...</p>
    if (error) return <p>{error}</p>

    return (
        <div>
            <h2>Tus Planes de Lectura</h2>
            <ul>
                {plans.map((plan) => (
                    <li key={plan.id}>
                        <h3>{plan.book.title}</h3>
                        <p>Páginas por día: {plan.pages_per_day}</p>

                    </li>

                ))}
            </ul>
        </div>
    );
};
export default ReadingPlanList