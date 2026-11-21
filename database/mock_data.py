
from datetime import date

from database.db import create_database, SessionLocal
from database.db import Customer, Order

# Create database and tables
create_database()

# Create database session
db = SessionLocal()

try:
    # Insert customers
    customers = [
        Customer(name="Ali", city="Tehran", age=28),
        Customer(name="Sara", city="Shiraz", age=32),
        Customer(name="Reza", city="Tehran", age=35),
        Customer(name="Mina", city="Isfahan", age=24),
    ]

    db.add_all(customers)
    db.commit()

    # Insert orders
    orders = [
        Order(customer_id=1, product="Laptop", amount=1200, order_date=date(2026, 1, 10)),
        Order(customer_id=1, product="Mouse", amount=50, order_date=date(2026, 1, 12)),
        Order(customer_id=2, product="Phone", amount=800, order_date=date(2026, 2, 5)),
        Order(customer_id=3, product="Laptop", amount=1200, order_date=date(2026, 2, 15)),
        Order(customer_id=4, product="Keyboard", amount=100, order_date=date(2026, 3, 1)),
    ]

    db.add_all(orders)
    db.commit()

    print("Sample data inserted successfully!")

finally:
    db.close()
