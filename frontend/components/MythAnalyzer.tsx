import React, { useState } from 'react';
import { analyzeMyth } from '@/lib/api';
import { VerdictCard } from './VerdictCard';
import { LoadingSpinner } from './LoadingSpinner';

interface AnalysisResult {
  claim: string;
  verdict: string;
  confidence_score: number;
  explanation: string;
}

export const MythAnalyzer: React.FC = () => {
  const [myth, setMyth] = useState('');
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<AnalysisResult | null>(null);
  const [error, setError] = useState('');

  const handleAnalyze = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!myth.trim()) {
      setError('Please enter a claim to analyze');
      return;
    }

    setLoading(true);
    setError('');
    setResult(null);

    try {
      const data = await analyzeMyth(myth);
      setResult(data);
    } catch (err) {
      setError(
        err instanceof Error ? err.message : 'Failed to analyze claim'
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="space-y-6">
      {/* Input Section */}
      <form onSubmit={handleAnalyze} className="bg-white rounded-lg shadow-lg p-8">
        <label htmlFor="myth-input" className="block text-sm font-semibold text-gray-700 mb-3">
          Enter a Claim to Analyze
        </label>
        <textarea
          id="myth-input"
          value={myth}
          onChange={(e) => setMyth(e.target.value)}
          placeholder="e.g., Vaccines cause autism. AI will replace all jobs. Drinking alkaline water cures diseases..."
          className="w-full px-4 py-3 border-2 border-slate-200 rounded-lg focus:outline-none focus:border-secondary resize-none"
          rows={4}
          disabled={loading}
        />
        <button
          type="submit"
          disabled={loading}
          className="mt-4 w-full bg-secondary hover:bg-indigo-700 disabled:bg-gray-400 text-white font-semibold py-3 px-6 rounded-lg transition-colors duration-200"
        >
          {loading ? 'Analyzing...' : 'Analyze Claim'}
        </button>
      </form>

      {/* Error Message */}
      {error && (
        <div className="bg-red-50 border-l-4 border-red-500 p-4 rounded">
          <p className="text-red-700 font-semibold">Error</p>
          <p className="text-red-600">{error}</p>
        </div>
      )}

      {/* Loading State */}
      {loading && <LoadingSpinner />}

      {/* Results Section */}
      {result && !loading && (
        <VerdictCard result={result} />
      )}
    </div>
  );
};
