

from models.customer import Customer
from models.restaurant import Restaurant
from models.review import Review

def seed_database():
    # Drop and recreate tables
    Customer.drop_table()
    Restaurant.drop_table()
    Review.drop_table()
    Customer.create_table()
    Restaurant.create_table()
    Review.create_table()

    # Sample Restaurants
    pizza_inn = Restaurant(name="Pizza Inn", address="123 Moi Ave, Nairobi", rating="4.5")
    mountain_delight = Restaurant(name="Mountain Delight", address="456 Hill Rd, Kiambu", rating="4.7")
    urban_eats = Restaurant(name="Urban Eats", address="789 China Square, Nairobi", rating="4.3")
    pizza_inn.save()
    mountain_delight.save()
    urban_eats.save()

    # Sample Customers
    alice = Customer(name="Alice", body="Loves pizza and open-air dining.")
    keith = Customer(name="Keith", body="Enjoys scenic views while dining.")
    lio = Customer(name="Lio", body="Prefers urban restaurant settings.")
    alice.save()
    keith.save()
    lio.save()
    
    
    # Sample Reviews
    Review.create(username="alice_j", comment="Amazing pizza and great ambiance!", restaurant_id=pizza_inn.id, customer_id=alice.id)
    Review.create(username="keith_s", comment="Breathtaking views and delicious food!", restaurant_id=mountain_delight.id, customer_id=keith.id)
    Review.create(username="lio_m", comment="Great vibe, but food was average.", restaurant_id=urban_eats.id, customer_id=lio.id)

  
    
    seed_database()
    print("Database seeded with initial data!")
