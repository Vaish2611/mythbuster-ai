# MythBuster AI - Setup Guide

## Project Structure

```
mythbuster-ai/
├── frontend/                 # Next.js/React frontend
│   ├── pages/               # Next.js pages
│   ├── components/          # React components
│   ├── lib/                 # Utilities and API client
│   ├── styles/              # Global styles
│   ├── public/              # Static assets
│   ├── package.json
│   ├── tsconfig.json
│   ├── next.config.js
│   ├── tailwind.config.js
│   └── postcss.config.js
│
├── backend/                 # FastAPI backend
│   ├── app/
│   │   ├── routes/          # API routes
│   │   ├── services/        # Business logic
│   │   ├── config.py        # Configuration
│   │   ├── models.py        # Pydantic models
│   │   └── main.py          # FastAPI app factory
│   ├── run.py               # Entry point
│   ├── requirements.txt
│   └── .env.example
│
├── .gitignore
└── SETUP_GUIDE.md
```

## Backend Setup

### Prerequisites
- Python 3.10+
- pip or conda

### Installation

1. **Navigate to backend directory:**
   ```bash
   cd backend
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Setup environment variables:**
   ```bash
   cp .env.example .env
   ```

5. **Run the server:**
   ```bash
   python run.py
   ```

   The API will be available at `http://localhost:8000`
   - API Docs: `http://localhost:8000/docs`
   - Health Check: `http://localhost:8000/health`

## Frontend Setup

### Prerequisites
- Node.js 18+
- npm or yarn

### Installation

1. **Navigate to frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Setup environment variables:**
   ```bash
   # Create .env.local (optional, defaults to http://localhost:8000)
   echo "NEXT_PUBLIC_API_URL=http://localhost:8000" > .env.local
   ```

4. **Run development server:**
   ```bash
   npm run dev
   ```

   The frontend will be available at `http://localhost:3000`

5. **Build for production:**
   ```bash
   npm run build
   npm start
   ```

## API Endpoints

### Health Check
- **GET** `/health`
  - Response: `{ "status": "healthy" }`

### Analyze Claim
- **POST** `/analyze`
  - Request Body:
    ```json
    {
      "claim": "Vaccines cause autism."
    }
    ```
  - Response:
    ```json
    {
      "claim": "Vaccines cause autism.",
      "verdict": "FALSE",
      "confidence_score": 0.98,
      "explanation": "Multiple large-scale studies have found no link between vaccines and autism."
    }
    ```

## Development Workflow

### Frontend Development
```bash
cd frontend
npm run dev              # Start dev server
npm run type-check      # Check TypeScript types
npm run lint            # Lint code
```

### Backend Development
```bash
cd backend
python run.py           # Start server (auto-reload on changes)
```

### Testing the Integration

1. Start backend: `python backend/run.py`
2. Start frontend: `npm run dev` (from frontend directory)
3. Navigate to `http://localhost:3000`
4. Enter a claim and click "Analyze Claim"

## Production Considerations

- **Backend**: Use production WSGI server (Gunicorn, etc.)
- **Frontend**: Build Next.js and deploy to static hosting or Next.js server
- **Environment Variables**: Secure all sensitive configs
- **CORS**: Configure allowed origins appropriately
- **Error Handling**: Implement proper logging and monitoring
- **Rate Limiting**: Add API rate limiting for production
- **Caching**: Implement response caching strategies

## Next Steps

1. Integrate actual LLM model for claim analysis
2. Add evidence discovery from multiple sources
3. Implement database for storing analysis history
4. Add user authentication
5. Create admin dashboard for managing agents
6. Implement visualization for misinformation timelines
