# PROJECT
# Restaurant Management CLI
It is a  CLI-based project to manage Restaurants, Customers, and Reviews. This tool provides functionalities to create, update, retrieve, and delete records in a SQLite database, using Python models with object-oriented programming principles.

### Requirements
Python 3.x
SQLite3

# SETUP
1.Clone the repository:
   ```txt
    git clone https://github.com/lio-web/new-python
    cd new-python

    ```

## Generating Your Environment

Install any additional dependencies you know you'll need by
adding them to the `Pipfile`. Then run the commands:

```console
pipenv install
pipenv shell
```
---
## Models and Methods
### Customer Model
| Method            | Description |
|-------------------|-------------|
| `create_table()`  | Creates the `customers` table. |
| `drop_table()`    | Drops the `customers` table. |
| `get_all()`       | Returns a list of all `Customer` records. |
| `find_by_id()`    | Returns a `Customer` object by its ID. |
| `find_by_name()`  | Returns a `Customer` object by its name. |
| `save()`          | Saves a new customer to the database and updates its `id`. |
| `update()`        | Updates the database entry for the `Customer` instance. |
| `delete()`        | Deletes the database entry for the `Customer` instance. |

### Restaurant Model
|Method |           | Description|               
|-------------------|-------------|
|`create_table()`	  |Creates the restaurants table.|
|`drop_table()`	  |Drops the restaurants table.|
|`get_all()`	     |Returns a list of all Restaurant records.|
|`find_by_id()`	  |Returns a Restaurant object by its ID.|
|`find_by_name()`	  |Returns a Restaurant object by its name.|
|`save()	`          |Saves a new restaurant to the database and updates its id.|
|`update()`	        |Updates the database entry for the Restaurant instance.|
|`delete()`	        |Deletes the database entry for the Restaurant instance.|

### Review Model
| Method           | Description |
|------------------|-------------|
| `create_table()` | Creates the `reviews` table. |
| `drop_table()`   | Drops the `reviews` table. |
| `get_all()`      | Returns a list of all `Review` records. |
| `find_by_id()`   | Returns a `Review` object by its ID. |
| `save()`         | Saves a new review to the database and updates its `review_id`. |
| `update()`       | Updates the database entry for the `Review` instance. |
| `delete()`       | Deletes the database entry for the `Review` instance. |


# Usage Examples
Here’s how to use the Customer, Restaurant, and Review models with the data.

Customer Model
```py
from models.customer import Customer

# Find customer by ID
alice = Customer.find_by_id(1)
print(alice)  # Output: <Customer 1: Alice>

# Update customer information
alice.body = "Loves pizza and outdoor seating."
alice.update()

# Retrieve all customers
customers = Customer.get_all()
print(customers)  # Output: [<Customer 1: Alice>, <Customer 2: Keith>, <Customer 3: Lio>]
```

Restaurant Model
```py
from models.restaurant import Restaurant

# Find restaurant by name
pizza_inn = Restaurant.find_by_name("Pizza Inn")
print(pizza_inn)  # Output: <Restaurant 1: Pizza Inn>

# Update restaurant rating
pizza_inn.rating = "4.6"
pizza_inn.update()

# Retrieve all restaurants
restaurants = Restaurant.get_all()
print(restaurants)  # Output: [<Restaurant 1: Pizza Inn>, <Restaurant 2: Mountain Delight>, <Restaurant 3: Urban Eats>]

```

Review Model
```py
from models.review import Review

# Retrieve all reviews
reviews = Review.get_all()
print(reviews)
# Output: [<Review 1: Amazing pizza and great ambiance!>, <Review 2: Breathtaking views and delicious food!>, <Review 3: Great vibe, but food was average.>]

# Update a review comment
review = Review.find_by_id(1)
review.comment = "Best pizza place I've visited!"
review.update()

# Delete a review
review.delete()
```

### Running the CLI
To interact with your database through the CLI, follow these steps:

Start the CLI
Run the CLI script (replace cli.py with your main file if necessary).
```txt
python cli.py
```

# Conclusion
This project provides a foundational structure for managing customers, restaurants, and reviews through a simple database model. Using this setup, you can easily create, update, retrieve, and delete records for each entity. The example usage and sample data demonstrate how to interact with the database and provide a good starting point for further development or customization.
