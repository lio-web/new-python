#!/usr/bin/env python3
# lib/debug.py

from models.restaurant import Restaurant
from models.review import Review
from models.customer import Customer
import ipdb

def reset_database():
    # Drop existing tables
    Customer.drop_table()
    Restaurant.drop_table()
    Review.drop_table()

    # Create tables in the correct order
    Customer.create_table()
    Restaurant.create_table()
    Review.create_table()

    # Insert seed data for Restaurant table
    pizza_inn = Restaurant.create(name="Pizza Inn", address="123 Moi Ave, Nairobi", rating="4.5")
    mountain_delight = Restaurant.create(name="Mountain Delight", address="456 Hill Rd, Kiambu", rating="4.7")
    urban_eats = Restaurant.create(name="Urban Eats", address="789 China Square, Nairobi", rating="4.3")

    # Insert seed data for Customer table
    alice = Customer.create(name="Alice", body="Loves pizza and open-air dining.")
    keith = Customer.create(name="Keith", body="Enjoys scenic views while dining.")
    Lio = Customer.create(name="Lio", body="Prefers urban restaurant settings.")

    # Insert seed data for Review table
    Review.create(username="alice_j", comment="Amazing pizza and great ambiance!", restaurant_id=pizza_inn.id, customer_id=alice.id)
    Review.create(username="keith_s", comment="Breathtaking views and delicious food!", restaurant_id=mountain_delight.id, customer_id=keith.id)
    Review.create(username="lio_m", comment="Great vibe, but food was average.", restaurant_id=urban_eats.id, customer_id=Lio.id)

# Run the reset_database function to initialize the database with seed data
reset_database()

# Open an interactive debugger at this point
ipdb.set_trace()
