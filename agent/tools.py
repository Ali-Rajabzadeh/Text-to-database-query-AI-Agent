
from langchain.tools import tool
from database.db import SessionLocal, Customer

@tool
def get_customer_by_id(customer_id: int) -> str:
    """Get customer information using their ID"""

    db = SessionLocal()

    try:
        customer = (
            db.query(Customer)
            .filter(Customer.id == customer_id)
            .first()
        )

        if customer is None:
            return f"No customer found with ID {customer_id}"

        return(
            f"ID: {customer.id},"
            f"Name: {customer.name},"
            f"City: {customer.city},"
            f"Age: {customer.age}"
        )

    finally:
        db.close()