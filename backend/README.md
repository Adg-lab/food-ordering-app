# Backend

## Installation

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate it:
```bash
# On Windows
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Setup

1. Run migrations:
```bash
python manage.py migrate
```

2. Create a superuser:
```bash
python manage.py createsuperuser
```

3. Load sample data (optional):
```bash
python manage.py loaddata sample_data
```

## Running the Server

```bash
python manage.py runserver 8000
```

Server will be available at `http://localhost:8000`
Admin interface at `http://localhost:8000/admin`
API at `http://localhost:8000/api/`
