# AI-Solutions Website

A Django-based website for AI-Solutions, showcasing software solutions and managing customer inquiries.

## Features
- Software solutions showcase
- Customer testimonials and ratings
- Articles and blog posts
- Photo galleries
- Contact form for customer inquiries
- Admin dashboard for managing inquiries
- Event management system

## Setup Instructions

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
- Windows:
```bash
venv\Scripts\activate
```
- Unix/MacOS:
```bash
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

## Project Structure
- `ai_solutions/` - Main project directory
- `core/` - Core application for main website features
- `admin/` - Admin dashboard application
- `static/` - Static files (CSS, JS, images)
- `templates/` - HTML templates
- `media/` - User-uploaded files

## Technologies Used
- Django 5.0.2
- Bootstrap 5
- Crispy Forms
- Pillow (for image handling) 