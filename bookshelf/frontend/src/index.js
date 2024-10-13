import React from 'react';
import ReactDOM from 'react-dom/client'; // Asegúrate de importar desde 'react-dom/client'
import App from './App';
import './index.css'; // Si tienes estilos

// Crea un contenedor raíz para tu aplicación
const root = ReactDOM.createRoot(document.getElementById('root'));

// Renderiza la aplicación dentro del contenedor raíz
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
