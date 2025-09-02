import React, { useState } from 'react';
import AuthCard from '../components/ui/AuthCard';
import Input from '../components/ui/Input';
import Button from '../components/ui/Button';

const Cadastro: React.FC = () => {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirm, setConfirm] = useState('');
  const [accept, setAccept] = useState(false);
  const [errors, setErrors] = useState<{ name?: string; email?: string; password?: string; confirm?: string }>({});

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const newErrors: { name?: string; email?: string; password?: string; confirm?: string } = {};
    if (!name) newErrors.name = 'Informe seu nome.';
    if (!email) newErrors.email = 'Informe seu email.';
    if (!password) newErrors.password = 'Informe sua senha.';
    if (confirm !== password) newErrors.confirm = 'As senhas não correspondem.';
    setErrors(newErrors);
    if (Object.keys(newErrors).length === 0) {
      try {
        const response = await fetch('http://localhost:5000/register', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ email, password }),
        });
        const data = await response.json();
        if (data.message) {
          window.location.href = '/login';
        } else {
          setErrors({ email: data.error || 'Falha no cadastro.' });
        }
      } catch (err) {
        setErrors({ email: 'Erro de conexão com o servidor.' });
      }
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-background px-4">
      <AuthCard title="Criar conta" subtitle="Cadastre-se para começar">
        <form className="space-y-6" onSubmit={handleSubmit}>
          <Input
            label="Nome completo"
            id="name"
            type="text"
            autoComplete="name"
            placeholder="Seu nome"
            value={name}
            onChange={(e) => setName(e.target.value)}
            error={errors.name}
          />
          <Input
            label="Email"
            id="email"
            type="email"
            autoComplete="email"
            placeholder="voce@example.com"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            error={errors.email}
          />
          <Input
            label="Senha"
            id="password"
            type="password"
            autoComplete="new-password"
            placeholder="********"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            hint="Mínimo 8 caracteres."
            error={errors.password}
          />
          <Input
            label="Confirmar senha"
            id="confirm"
            type="password"
            autoComplete="new-password"
            placeholder="********"
            value={confirm}
            onChange={(e) => setConfirm(e.target.value)}
            error={errors.confirm}
          />
          <label className="flex items-center space-x-2 text-sm">
            <input
              type="checkbox"
              className="rounded border"
              checked={accept}
              onChange={(e) => setAccept(e.target.checked)}
            />
            <span>Aceito os Termos e a Política de Privacidade</span>
          </label>
          <Button type="submit">Criar conta</Button>
          <div className="text-center text-sm text-muted-foreground">
            Já tem conta?{' '}
            <a href="/login" className="font-medium text-primary">
              Entrar
            </a>
          </div>
        </form>
      </AuthCard>
    </div>
  );
};

export default Cadastro;
