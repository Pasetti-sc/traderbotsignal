import React from 'react';
import Login from './pages/Login';
import Cadastro from './pages/Cadastro';
import Dashboard from './pages/Dashboard';

function App() {
  const pathname = window.location.pathname;
  switch (pathname) {
    case '/cadastro':
      return <Cadastro />;
    case '/dashboard':
      return <Dashboard />;
    case '/':
    case '/login':
    default:
      return <Login />;
  }
}

export default App;
