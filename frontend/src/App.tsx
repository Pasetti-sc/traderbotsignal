import React from 'react';
import Login from './pages/Login';
import Cadastro from './pages/Cadastro';

function App() {
  const pathname = window.location.pathname;
  switch (pathname) {
    case '/cadastro':
      return <Cadastro />;
    case '/login':
    default:
      return <Login />;
  }
}

export default App;
