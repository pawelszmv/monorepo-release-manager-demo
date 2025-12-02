import React from 'react';
import packageJson from '../package.json';

export default function App() {
  return (
    <div className="app">
      <header>
        <h1>FE Web (React)</h1>
        <p>Version: {packageJson.version}</p>
      </header>
      <main>
        <p>This is a minimal React app scaffolded with Vite.</p>
        <button onClick={() => alert('hello from FE Web')}>Say hello</button>
      </main>
    </div>
  );
}