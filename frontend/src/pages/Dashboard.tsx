import React from 'react';
import TradingViewWidget from '../components/TradingViewWidget';
import Button from '../components/ui/Button';

const Dashboard: React.FC = () => {
  const user = {
    name: 'Usuário',
    email: 'usuario@example.com',
  };

  return (
    <div className="min-h-screen bg-background text-gray-800">
      <header className="flex items-center justify-between bg-card p-4 shadow">
        <h1 className="text-xl font-bold">TraderBot</h1>
        <div className="flex items-center space-x-4">
          <div className="text-right text-sm">
            <div>{user.name}</div>
            <div className="text-muted-foreground">{user.email}</div>
          </div>
          <Button className="w-auto" onClick={() => (window.location.href = '/config')}>Configurações</Button>
        </div>
      </header>
      <main className="space-y-6 p-4">
        <div className="h-96 w-full">
          <TradingViewWidget />
        </div>
        <div className="grid grid-cols-1 gap-4 md:grid-cols-2">
          <div className="rounded-lg bg-card p-4 shadow">
            <h2 className="mb-2 text-lg font-semibold">Catalogador de Sinais</h2>
            <p className="text-sm text-muted-foreground">
              Conteúdo de análise de sinais históricos.
            </p>
          </div>
          <div className="rounded-lg bg-card p-4 shadow">
            <h2 className="mb-2 text-lg font-semibold">Análise em Tempo Real</h2>
            <p className="text-sm text-muted-foreground">
              Conteúdo de análise em tempo real.
            </p>
          </div>
        </div>
      </main>
    </div>
  );
};

export default Dashboard;

