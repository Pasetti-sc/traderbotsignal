import React from 'react';

interface InputProps extends React.InputHTMLAttributes<HTMLInputElement> {
  label: string;
  error?: string;
  hint?: string;
}

const Input = React.forwardRef<HTMLInputElement, InputProps>(
  ({ label, id, type = 'text', error, hint, className = '', ...props }, ref) => {
    const baseClass = `w-full rounded-lg border px-3 py-2 text-sm outline-none focus:ring-2 focus:ring-primary focus:border-transparent ${error ? 'border-red-500' : ''} ${className}`;
    return (
      <div className="space-y-1">
        <label htmlFor={id} className="block text-sm font-medium mb-1">
          {label}
        </label>
        <input id={id} ref={ref} type={type} className={baseClass} {...props} />
        {error ? (
          <p className="mt-1 text-xs text-red-600 dark:text-red-400">{error}</p>
        ) : hint ? (
          <p className="mt-1 text-xs text-muted-foreground">{hint}</p>
        ) : null}
      </div>
    );
  }
);

Input.displayName = 'Input';

export default Input;
