import React, { useState } from 'react';
import { MythAnalyzer } from '@/components/MythAnalyzer';

export default function Home() {
  return (
    <main className="min-h-screen bg-gradient-to-br from-slate-900 to-slate-800">
      <div className="container mx-auto px-4 py-12">
        <div className="text-center mb-12">
          <h1 className="text-5xl font-bold text-white mb-4">
            🔍 MythBuster AI
          </h1>
          <p className="text-xl text-slate-300">
            Uncover the truth behind popular claims
          </p>
        </div>

        <div className="max-w-2xl mx-auto">
          <MythAnalyzer />
        </div>
      </div>
    </main>
  );
}
