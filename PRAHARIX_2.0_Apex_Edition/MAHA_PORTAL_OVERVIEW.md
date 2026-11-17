# Maharashtra District Administrative Portal

## Overview
This is a starter **Django** based web application that provides a unified administrative portal for all districts of Maharashtra. It includes:
- Role‑based authentication (state admin, district admin, staff)
- CRUD for district‑level services (e.g., public utilities, permits)
- Multilingual support (Marathi, Hindi, English)
- Dashboard with basic analytics per district
- Responsive UI using **Bootstrap 5**
- Docker configuration for easy deployment on any cloud (AWS, Azure, GCP) or on‑premises servers.

## Folder Structure
```
maha_portal/                 # Django project root
├─ maha_portal/              # Settings, URLs, WSGI
│   ├─ __init__.py
│   ├─ settings.py
│   ├─ urls.py
│   └─ wsgi.py
├─ districts/                # Core app handling districts & services
│   ├─ migrations/
│   ├─ templates/districts/
│   ├─ __init__.py
│   ├─ admin.py
│   ├─ apps.py
│   ├─ models.py
│   ├─ urls.py
│   └─ views.py
├─ users/                    # Custom user model & auth logic
│   ├─ __init__.py
│   ├─ admin.py
│   ├─ apps.py
│   ├─ models.py
│   ├─ forms.py
│   └─ views.py
├─ static/                   # CSS/JS (Bootstrap, custom styles)
├─ templates/                # Base templates
│   └─ base.html
├─ manage.py
├─ Dockerfile                # Container build
└─ requirements.txt
```

## Quick Start
1. **Prerequisites** – Install Docker **or** have Python 3.10+ and PostgreSQL installed.
2. Clone this repo (or copy the generated folder) into your workspace.
3. Create a virtual environment and install requirements:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # Windows PowerShell
   pip install -r requirements.txt
   ```
4. Apply migrations and create a superuser:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```
5. Run the development server:
   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```
   Visit `http://localhost:8000/`.
6. For production, build the Docker image:
   ```bash
   docker build -t maha-portal .
   docker run -p 8000:8000 maha-portal
   ```

## Extending the Portal
- **Add new services** – Create a model in `districts/models.py` and register it in `admin.py`.
- **Integrate with existing gov APIs** – Write wrappers in `districts/services.py` and call them from views.
- **GIS mapping** – Use `django-leaflet` and the provided `DistrictLocation` model.
- **Reporting** – Extend `dashboard/views.py` and use `django-report-builder` for PDF/Excel exports.

---
*This document lives in the artifact directory and serves as the project’s README.*
