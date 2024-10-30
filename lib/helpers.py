from models.customer import Customer
from models.restaurant import Restaurant
from models.review import Review


def exit_program():
    print("It was nice having you around!")
    exit()


# Restaurant functions
def list_restaurants():  # Lists all restaurants in the database
    restaurants = Restaurant.get_all()
    if not restaurants:
        print("No restaurants found.")
    else:
        for restaurant in restaurants:
            print(restaurant)


def find_restaurant_by_name():                      #Finds a restaurant by name.
    name = input("Enter the restaurant's name: ")
    restaurant = Restaurant.find_by_name(name)
    print(restaurant) if restaurant else print(f"Restaurant '{name}' not found.")


def find_restaurant_by_id():   #Finds a restaurant by its ID.
    id_ = input("Enter the restaurant's ID: ")
    restaurant = Restaurant.find_by_id(id_)
    print(restaurant) if restaurant else print(f"Restaurant with ID {id_} not found.")


def create_restaurant():   #Creates a new restaurant entry with user-provided details.
    name = input("Enter the restaurant name: ")
    address = input("Enter the restaurant address: ")
    rating = input("Enter the restaurant rating: ")

    try:
        new_restaurant = Restaurant.create(name=name, address=address, rating=rating)
        print(f"Restaurant '{name}' has been created with ID {new_restaurant.id}.")
    except Exception as e:
        print(f"Error creating a restaurant: {e}")


def update_restaurant():   #Updates details of an existing restaurant.
    id_ = input("Enter the restaurant's ID: ")
    restaurant = Restaurant.find_by_id(id_)
    if restaurant:
        try:
            name = input("Enter the restaurant's new name: ")
            address = input("Enter the restaurant's new address: ")
            rating = input("Enter the restaurant's new rating: ")

            restaurant.name = name
            restaurant.address = address
            restaurant.rating = rating
            restaurant.update()
            print(f"Updated restaurant: {restaurant}")
        except Exception as e:
            print("Error updating restaurant:", e)
    else:
        print(f"Restaurant with ID {id_} not found.")


def delete_restaurant():   #Deletes a restaurant by ID.
    id_ = input("Enter the restaurant's ID: ")
    restaurant = Restaurant.find_by_id(id_)
    if restaurant:
        try:
            restaurant.delete()
            print("Restaurant deleted.")
        except Exception as e:
            print("Error deleting restaurant:", e)
    else:
        print(f"Restaurant with ID {id_} not found.")


# Customer functions
def list_customers():  #Lists all customers in the database.
    name = input("Enter customer name: ")
    customers = Customer.get_all()
    if not customers:
        print("No customers found.")
    else:
        for customer in customers:
            print(customer)


def find_customer_by_name(): #Finds a customer by name.
    name = input("Enter customer name: ")
    customer = Customer.find_by_name(name)
    print(customer) if customer else print(f"Customer '{name}' not found.")


def find_customer_by_id():  #Finds a customer by their ID.
    id_ = input("Enter the customer's ID: ")
    customer = Customer.find_by_id(id_)
    print(customer) if customer else print(f"Customer with ID {id_} not found.")


def create_customer():  #Creates a new customer entry with user-provided details.
    name = input("Enter the customer's name: ")
    body = input("Enter the customer's details: ")
    try:
        new_customer = Customer.create(name=name, body=body)
        print(f"Customer '{name}' has been created with ID {new_customer.id}.")
    except Exception as e:
        print("Error creating customer:", e)


def update_customer():  #Updates details of an existing customer.
    id_ = input("Enter the customer's ID: ")
    customer = Customer.find_by_id(id_)
    if customer:
        try:
            name = input("Enter the customer's new name: ")
            body = input("Enter the customer's new details: ")

            customer.name = name
            customer.body = body
            customer.update()
            print(f"Updated customer: {customer}")
        except Exception as e:
            print("Error updating customer:", e)
    else:
        print(f"Customer with ID {id_} not found.")


def delete_customer():  #Deletes a customer by ID.
    id_ = input("Enter the customer's ID: ")
    customer = Customer.find_by_id(id_)
    if customer:
        try:
            customer.delete()
            print("Customer deleted.")
        except Exception as e:
            print("Error deleting customer:", e)
    else:
        print(f"Customer with ID {id_} not found.")


def list_reviews():  #Lists all reviews in the database.
    reviews = Review.get_all()
    if not reviews:
        print("No reviews found.")
    else:
        for review in reviews:
            print(review)
        


def find_review_by_id():               #Finds a review by its ID.
    id_ = input("Enter the review's ID: ")
    review = Review.find_by_id(id_)
    print(review) if review else print(f"Review with ID {id_} not found.")


def create_review(): #"Lists all reviews in the database.
    username = input("Enter the username: ")
    comment = input("Enter the comment: ")
    restaurant_id = int(input("Enter the restaurant ID: "))
    customer_id = int(input("Enter the customer ID: "))
    try:
        new_review = Review.create(username=username, comment=comment, restaurant_id=restaurant_id, customer_id=customer_id)
        print(f"Review created with ID {new_review.review_id}.")
    except Exception as e:
        print("Error creating review:", e)


def update_review():    #Updates details of an existing review.                  
    id_ = input("Enter the review's ID: ")
    review = Review.find_by_id(id_)
    print(review)
    if review:
        try:
            username = input("Enter the new username: ")
            comment = input("Enter the new comment: ")
            restaurant_id = int(input("Enter the new restaurant ID: "))
            customer_id = int(input("Enter the new customer ID: "))

            review.username = username
            review.comment = comment
            review.restaurant_id = restaurant_id
            review.customer_id = customer_id
            print(review.username, review.comment,review.restaurant_id,review.customer_id)
            review.update()
            print(f"Updated review: {review}")
        except Exception as e:
            print("Error updating review:", e)
    else:
        print(f"Review with ID {id_} not found.")
        
        


def delete_review():#Deletes a review by ID.
    id_ = input("Enter the review's ID: ")
    review = Review.find_by_id(id_)
    if review:
        try:
            review.delete()
            print("Review deleted.")
        except Exception as e:
            print("Error deleting review:", e)
    else:
        print(f"Review with ID {id_} not found.")
