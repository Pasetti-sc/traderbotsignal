import React from 'react';

interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: 'primary' | 'ghost';
}

const Button: React.FC<ButtonProps> = ({ variant = 'primary', className = '', ...props }) => {
  const base = 'inline-flex w-full items-center justify-center rounded-lg px-4 py-2 text-sm font-medium focus:outline-none disabled:opacity-60';
  const variants: Record<string, string> = {
    primary: 'bg-primary text-primary-foreground hover:opacity-90',
    ghost: 'border hover:bg-accent',
  };
  return <button className={`${base} ${variants[variant]} ${className}`} {...props} />;
};

export default Button;
