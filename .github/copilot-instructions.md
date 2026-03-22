# GitHub Copilot Custom Instructions

This is a food ordering web application project with a React + TypeScript frontend and Django backend.

## Project Structure
- **frontend/**: React + TypeScript application using Vite
- **backend/**: Django REST API with models for menu items and orders

## Key Technologies
- Frontend: React 18, TypeScript, Vite, React Router
- Backend: Django 4.2, Django REST Framework, SQLite

## Development Workflow
1. Frontend runs on http://localhost:3000
2. Backend API runs on http://localhost:8000
3. Frontend proxies API calls to backend during development

## Important Notes
- CORS is configured to allow localhost:3000
- Database is SQLite (development)
- Images are handled with Pillow
- Both services support hot-reload during development
