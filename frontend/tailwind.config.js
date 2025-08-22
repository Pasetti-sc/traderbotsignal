/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './public/index.html',
    './src/**/*.{js,jsx,ts,tsx}',
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        background: '#f9fafb',
        card: '#ffffff',
        primary: '#2563eb',
        'primary-foreground': '#ffffff',
        accent: '#e5e7eb',
        'muted-foreground': '#6b7280',
      },
    },
  },
  plugins: [],
};

