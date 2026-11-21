from database.db import SessionLocal, Customer, Order

db = SessionLocal()

try:
    # 1. Get all customers
    customers = db.query(Customer).all()

    for customer in customers:
        print(customer.name, customer.city, customer.age)

    print("\n-------------------")

    #2. Find customers from Tehran

    tehran_customers = (
        db.query(Customer).filter(Customer.city == "Tehran").all()
        )

    for customer in tehran_customers:
        print(customer.name)

    print("\n-------------------")

    # 3. Calculate total order amount
    order_numb = (db.query(Order.amount).all())
    total = int()
    for orders in order_numb:
        total += orders[0]

    print(f"total order amount is: {total}")

finally:
    db.close()