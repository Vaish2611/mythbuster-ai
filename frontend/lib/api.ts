import axios from 'axios';

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

const apiClient = axios.create({
  baseURL: API_URL,
  timeout: 30000,
});

interface AnalyzeResponse {
  claim: string;
  verdict: string;
  confidence_score: number;
  explanation: string;
}

export const analyzeMyth = async (myth: string): Promise<AnalyzeResponse> => {
  try {
    const response = await apiClient.post<AnalyzeResponse>('/analyze', {
      claim: myth,
    });
    return response.data;
  } catch (error) {
    if (axios.isAxiosError(error) && error.response) {
      throw new Error(
        error.response.data?.detail || 'Failed to analyze the claim'
      );
    }
    throw new Error('Network error. Please try again.');
  }
};
