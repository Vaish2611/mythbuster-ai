import React from 'react';

interface VerdictCardProps {
  result: {
    claim: string;
    verdict: string;
    confidence_score: number;
    explanation: string;
  };
}

const verdictColors: Record<string, { bg: string; text: string; icon: string }> = {
  TRUE: { bg: 'bg-green-50', text: 'text-green-700', icon: '✓' },
  'MOSTLY TRUE': { bg: 'bg-lime-50', text: 'text-lime-700', icon: '✓' },
  MIXED: { bg: 'bg-yellow-50', text: 'text-yellow-700', icon: '◐' },
  'MOSTLY FALSE': { bg: 'bg-orange-50', text: 'text-orange-700', icon: '✗' },
  FALSE: { bg: 'bg-red-50', text: 'text-red-700', icon: '✗' },
  'INSUFFICIENT EVIDENCE': {
    bg: 'bg-gray-50',
    text: 'text-gray-700',
    icon: '?',
  },
};

export const VerdictCard: React.FC<VerdictCardProps> = ({ result }) => {
  const verdictStyle = verdictColors[result.verdict] || verdictColors.MIXED;
  const confidencePercentage = Math.round(result.confidence_score * 100);

  return (
    <div className="space-y-4">
      {/* Verdict */}
      <div className={`${verdictStyle.bg} border-l-4 rounded-lg p-6`}>
        <div className="flex items-start justify-between">
          <div>
            <h3 className="text-lg font-semibold text-gray-900 mb-2">
              Claim
            </h3>
            <p className="text-gray-700 mb-4">{result.claim}</p>
          </div>
        </div>

        <div className={`${verdictStyle.text} font-bold text-2xl mb-4`}>
          {verdictStyle.icon} {result.verdict}
        </div>

        {/* Confidence Score */}
        <div className="mb-4">
          <div className="flex justify-between items-center mb-2">
            <span className="text-sm font-semibold text-gray-700">
              Confidence Score
            </span>
            <span className="text-sm font-bold text-gray-900">
              {confidencePercentage}%
            </span>
          </div>
          <div className="w-full bg-gray-200 rounded-full h-2">
            <div
              className={`${
                confidencePercentage >= 75
                  ? 'bg-green-500'
                  : confidencePercentage >= 50
                  ? 'bg-yellow-500'
                  : 'bg-red-500'
              } h-2 rounded-full transition-all duration-300`}
              style={{ width: `${confidencePercentage}%` }}
            />
          </div>
        </div>

        {/* Explanation */}
        <div>
          <h4 className="text-sm font-semibold text-gray-900 mb-2">
            Explanation
          </h4>
          <p className="text-gray-700 leading-relaxed">{result.explanation}</p>
        </div>
      </div>
    </div>
  );
};
