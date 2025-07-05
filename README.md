# ExpenseIncomeTracker API

This is a Django REST API project for tracking personal income and expenses. It includes user authentication via JWT and supports creating, listing, updating, and deleting income/expense records.

---

## Features

###  Authentication (JWT Based)

* User registration
* User login (JWT token generation)
* Token refresh

###  Expense & Income Tracker

* Add new income or expense entries
* List all entries (user-specific)
* Retrieve, update, and delete individual entries
* Automatically calculates totals including tax (flat or percentage)

###  OpenAPI Schema & Swagger UI

* DRF Spectacular integration
* Swagger UI at `/api/schema/swagger-ui/`
* ReDoc at `/api/schema/redoc/`

---

## 📁 Project Structure

```bash
ExpenseIncomeTracker/
├── ExpenseIncomeApp/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   └── ...
├── authenticate/
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── ...
├── ExpenseIncomeTracker/
│   ├── settings.py
│   ├── urls.py
│   └── ...
```

---

##  Authentication API

**Base URL**: `/api/auth/`

| Method | Endpoint     | Description          |
| ------ | ------------ | -------------------- |
| POST   | `/register/` | Register a new user  |
| POST   | `/login/`    | Get JWT tokens       |
| POST   | `/refresh/`  | Refresh access token |

**Register**

```json
POST /api/auth/register/
{
  "username": "exampleuser",
  "password": "securepassword",
  "confirm_password": "securepassword"
}
```

**Login**

```json
POST /api/auth/login/
{
  "username": "exampleuser",
  "password": "securepassword"
}
```

Response:

```json
{
  "refresh": "<token>",
  "access": "<token>"
}
```

---

## Expense & Income API

**Base URL**: `/api/expenses/`

| Method | Endpoint                       | Description              |
| ------ | ------------------------------ | ------------------------ |
| GET    | `/expense-income/`             | List all income/expenses |
| POST   | `/expense-income/`             | Create a new entry       |
| GET    | `/expense-income-detail/<id>/` | Retrieve single entry    |
| PUT    | `/expense-income-detail/<id>/` | Update single entry      |
| DELETE | `/expense-income-detail/<id>/` | Delete single entry      |

**Example Create Payload:**

```json
POST /api/expenses/expense-income/
{
  "title": "Freelance Payment",
  "description": "Web dev project",
  "amount": 1000,
  "transaction_type": "credit",
  "tax": 5,
  "tax_type": "percentage"
}
```

Each record automatically calculates the `total` field based on the `tax_type`.

* `flat`: total = amount + tax
* `percentage`: total = amount + (amount \* tax / 100)

---

##  Setup Instructions

1. **Clone repo**

```bash
git clone <repo_url>
cd ExpenseIncomeTracker
```

2. **Create virtual environment & install dependencies**

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

3. **Run migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

4. **Create a superuser**

```bash
python manage.py createsuperuser
```

5. **Start the development server**

```bash
python manage.py runserver
```

---

##  Settings Overview

* **JWT Auth**: `rest_framework_simplejwt`
* **Schema**: `drf_spectacular`
* **Pagination**: `PageNumberPagination`, page size = 10
* **Apps Installed**:

  * `authenticate`
  * `ExpenseIncomeApp`
  * `drf_spectacular`
  * `drf_spectacular_sidecar`

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Your Project API',
    'DESCRIPTION': 'Your project description',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'SWAGGER_UI_DIST': 'SIDECAR',
    'SWAGGER_UI_FAVICON_HREF': 'SIDECAR',
    'REDOC_DIST': 'SIDECAR',
}
```

---

##  API Documentation

Swagger UI:

```
http://127.0.0.1:8000/api/schema/swagger-ui/
```

ReDoc:

```
http://127.0.0.1:8000/api/schema/redoc/
```

---


