# Food Ordering Web App

A full-stack food ordering system for a school restaurant built with React + TypeScript (frontend) and Django + Python (backend).

## Project Structure

```
food-ordering-app/
├── frontend/              # React + TypeScript application
│   ├── src/
│   │   ├── App.tsx
│   │   ├── App.css
│   │   ├── main.tsx
│   │   └── index.css
│   ├── package.json
│   ├── tsconfig.json
│   ├── vite.config.ts
│   └── index.html
├── backend/               # Django REST API
│   ├── foodorder_project/ # Django project settings
│   ├── api/               # API app with models, views, serializers
│   ├── manage.py
│   ├── requirements.txt
│   └── README.md
├── .env                   # Environment variables
└── README.md
```

## Tech Stack

### Frontend
- **React 18** - UI library
- **TypeScript** - Type safety
- **Vite** - Build tool and dev server
- **React Router** - Client-side routing
- **Axios** - HTTP client

### Backend
- **Django 4.2** - Web framework
- **Django REST Framework** - REST API
- **SQLite** - Database (development)
- **Pillow** - Image handling
- **django-cors-headers** - Cross-origin requests

## Getting Started

### Prerequisites
- Node.js 16+ and npm
- Python 3.8+

### Frontend Setup

1. Navigate to frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start development server:
```bash
npm run dev
```

The app will run at `http://localhost:3000`

### Backend Setup

1. Navigate to backend directory:
```bash
cd backend
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate virtual environment:
```bash
# Windows
venv\Scripts\activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Create superuser (admin account):
```bash
python manage.py createsuperuser
```

7. Start the development server:
```bash
python manage.py runserver 8000
```

The API will run at `http://localhost:8000`
Admin panel at `http://localhost:8000/admin`

## API Endpoints

- `GET /api/menu-items/` - List all available menu items
- `GET /api/menu-items/by_category/?category=meals` - Get items by category
- `GET /api/orders/` - List all orders
- `GET /api/orders/pending/` - Get pending orders
- `POST /api/orders/` - Create a new order

## Features

- Browse restaurant menu organized by category
- Place food orders with multiple items
- Track order status (Pending, Preparing, Ready, Completed)
- Admin panel to manage menu items and orders
- Responsive design with modern UI

## Development

Both frontend and backend support hot-reload during development:

- **Frontend**: Changes to React components auto-refresh
- **Backend**: Django development server auto-reloads on code changes

## Next Steps

1. Design UI components and pages for:
   - Menu listing/browsing
   - Shopping cart
   - Checkout and order placement
   - Order tracking

2. Add authentication for:
   - Student login
   - Admin login

3. Enhance backend with:
   - Payment processing
   - Email notifications
   - Advanced filtering and search

4. Deploy to production

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
