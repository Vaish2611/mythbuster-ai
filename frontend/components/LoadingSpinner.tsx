import React from 'react';

export const LoadingSpinner: React.FC = () => {
  return (
    <div className="flex justify-center items-center py-12">
      <div className="flex flex-col items-center space-y-4">
        <div className="animate-spin">
          <div className="h-12 w-12 border-4 border-secondary border-t-transparent rounded-full" />
        </div>
        <p className="text-gray-400 font-semibold">Analyzing claim...</p>
      </div>
    </div>
  );
};
