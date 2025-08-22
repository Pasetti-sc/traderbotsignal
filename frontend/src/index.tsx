import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

const rootElement = document.documentElement;
const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)');
const handleThemeChange = (e: MediaQueryList | MediaQueryListEvent) => {
  rootElement.classList.toggle('dark', e.matches);
};

handleThemeChange(mediaQuery);
mediaQuery.addEventListener('change', handleThemeChange);

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
