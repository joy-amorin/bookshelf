import React from 'react';
import ReactDOM from 'react-dom/client'; 
import App from './App';
import './style/index.css';

// Crea un contenedor raíz para tu aplicación
const root = ReactDOM.createRoot(document.getElementById('root'));

// Renderiza la aplicación dentro del contenedor raíz
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
