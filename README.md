# Cafe Order Management System

A Django-based web application to manage cafe orders.

## Features
- Display all available items and their prices on the home page.
- Add, delete, search, and update orders.
- Automatically calculate total order cost.
- Track order status (pending, ready, paid).
- Calculate revenue for paid orders for a single shift and a total revenue for all the shifts.

## Setup
1. create a virtual environment in a any folder of you choosing.
   ```bash
    pip install virtualenv
   
   ## for windows 
   
      python -m venv .venv
      .\.venv\Scripts\activate
   
   ## for linux/mac
      python3 -m venv .venv
      source .venv/bin/activate

2. Clone the repository.
   ```bash
      git clone 
3. Install dependencies:
   ```bash
   pip install django


## Access the API Endpoints
Since we registered our routes using DefaultRouter() in urls.py, the API endpoints should be:
## Similarly, for items:
Get all items → http://127.0.0.1:8000/api/items/ 

Get a specific item → http://127.0.0.1:8000/api/items/{id}/

Create an item (POST) → http://127.0.0.1:8000/api/items/

Update an item (PUT/PATCH) → http://127.0.0.1:8000/api/items/{id}/

Delete an item (DELETE) → http://127.0.0.1:8000/api/items/{id}/

## Similarly, for orders:

Get all orders → http://127.0.0.1:8000/api/orders/

Get a specific order → http://127.0.0.1:8000/api/orders/{id}/

Create an order (POST) → http://127.0.0.1:8000/api/orders/

Update an order (PUT/PATCH) → http://127.0.0.1:8000/api/orders/{id}/

Delete an order (DELETE) → http://127.0.0.1:8000/api/orders/{id}/