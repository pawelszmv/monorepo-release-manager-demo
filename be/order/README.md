# Order Management Service

This project is an Order Management Service built using FastAPI. It provides a RESTful API for managing orders, including functionalities for creating, retrieving, updating, and deleting orders.

## Project Structure

```
be
└── order
    ├── app
    │   ├── main.py                # Entry point of the application
    │   ├── api
    │   │   └── v1
    │   │       ├── endpoints
    │   │       │   └── orders.py  # Order-related API endpoints
    │   │       └── __init__.py
    │   ├── core
    │   │   ├── config.py          # Configuration settings
    │   │   └── security.py        # Security-related functions
    │   ├── db
    │   │   ├── base.py            # Base class for database models
    │   │   └── session.py         # Database session management
    │   ├── models
    │   │   └── order.py           # Order model definition
    │   ├── schemas
    │   │   └── order.py           # Pydantic schemas for order validation
    │   ├── services
    │   │   └── order_service.py    # Business logic for managing orders
    │   ├── repositories
    │   │   └── order_repository.py  # Data access for orders
    │   └── __init__.py
    ├── tests
    │   ├── __init__.py
    │   └── test_orders.py         # Unit tests for order functionality
    ├── migrations
    │   └── versions               # Migration scripts for database changes
    ├── alembic.ini                # Alembic configuration file
    ├── Dockerfile                  # Docker image instructions
    ├── pyproject.toml             # Project configuration
    ├── requirements.txt            # Python dependencies
    ├── .env.example                # Example environment variables
    └── README.md                   # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd order
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Copy `.env.example` to `.env` and update the values as needed.

5. **Run the application:**
   ```
   uvicorn app.main:app --reload
   ```

## Usage

The API provides the following endpoints for managing orders:

- **Create Order:** `POST /api/v1/orders`
- **Get Order:** `GET /api/v1/orders/{order_id}`
- **Update Order:** `PUT /api/v1/orders/{order_id}`
- **Delete Order:** `DELETE /api/v1/orders/{order_id}`
- **List Orders:** `GET /api/v1/orders`

## Testing

To run the tests, use the following command:

```
pytest
```

## License

This project is licensed under the MIT License.