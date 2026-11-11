# Smart HR & Employee Management System

A Django-based HR management application starter for an internship project.

## Current scope
- Custom user roles: Admin, HR, Employee
- Employee and department records
- Attendance check-in/check-out
- Leave requests and HR approval
- Payroll records with employee-only payslip access
- Dashboard and CSV reports (planned/incremental)

> This is an initial runnable foundation, not a claim that every listed workflow is complete.

## Requirements
- Python 3.11+
- pip
- SQLite for quick local development; PostgreSQL can be configured later

## Setup (Windows PowerShell)
```powershell
py -3.11 -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Open http://127.0.0.1:8000/

## Tests
```powershell
python manage.py test
```

## Security notes
- Set a unique `SECRET_KEY` and `DEBUG=False` in production.
- Never commit `.env`, credentials, real employee data, or payslips.
- Use synthetic demo data only.
