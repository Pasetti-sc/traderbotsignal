import React, { useState } from 'react';
import AuthCard from '../components/ui/AuthCard';
import Input from '../components/ui/Input';
import Button from '../components/ui/Button';

const Login: React.FC = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [remember, setRemember] = useState(false);
  const [errors, setErrors] = useState<{ email?: string; password?: string }>({});

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    const newErrors: { email?: string; password?: string } = {};
    if (!email) newErrors.email = 'Informe seu email.';
    if (!password) newErrors.password = 'Informe sua senha.';
    setErrors(newErrors);
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-background px-4">
      <AuthCard title="Entrar" subtitle="Acesse sua conta">
        <form className="space-y-6" onSubmit={handleSubmit}>
          <Input
            label="Email"
            id="email"
            type="email"
            autoComplete="username"
            placeholder="voce@example.com"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            error={errors.email}
          />
          <Input
            label="Senha"
            id="password"
            type="password"
            autoComplete="current-password"
            placeholder="********"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            error={errors.password}
          />
          <div className="flex items-center justify-between">
            <label className="flex items-center space-x-2 text-sm">
              <input
                type="checkbox"
                className="rounded border"
                checked={remember}
                onChange={(e) => setRemember(e.target.checked)}
              />
              <span>Lembrar de mim</span>
            </label>
            <a href="#" className="text-sm font-medium text-primary hover:underline">
              Esqueci minha senha
            </a>
          </div>
          <Button type="submit">Entrar</Button>
          <div className="text-center text-sm text-muted-foreground">
            Não tem conta?{' '}
            <a href="/cadastro" className="font-medium text-primary">
              Cadastre-se
            </a>
          </div>
          <div className="text-center text-xs text-muted-foreground">
            Integração com API virá aqui
          </div>
        </form>
      </AuthCard>
    </div>
  );
};

export default Login;
