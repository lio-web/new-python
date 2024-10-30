from models.__init__ import CURSOR, CONN
from models.restaurant import Restaurant  
from models.customer import Customer
# from datetime import datetime

id
class Review:
    all = {}

    def __init__(self, review_id, username, comment, created_at, restaurant_id, customer_id):
        self.review_id = review_id
        self.username = username
        self.comment = comment
        self.created_at = created_at
        self.restaurant_id = restaurant_id
        self.customer_id = customer_id
       
    def __repr__(self):
        return f"<Review {self.review_id}: {self.customer_id} - {self.comment}>"

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        value = value.strip() 
        if isinstance(value, str) and value:
            self._username = value
        else:
            raise ValueError("Username must be a non-empty string")

    @property
    def comment(self):
        return self._comment

    @comment.setter
    def comment(self, value):
        value = value.strip()  # Trim whitespace
        if isinstance(value, str):
            self._comment = value
        else:
            raise ValueError("Comment must be a string")

    @property
    def restaurant_id(self):
        return self._restaurant_id

    @restaurant_id.setter
    def restaurant_id(self, restaurant_id):
        if isinstance(restaurant_id, int) :
            self._restaurant_id = restaurant_id
        else:
            raise ValueError("restaurant_id must reference a restaurant in the database")

    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        if isinstance(value, int) and value > 0:
            self._customer_id = value
        else:
            raise ValueError("Customer ID must be a positive integer")
        
    @classmethod
    def get_all(cls):
        """Return a list containing one Review object per table row"""
        sql = """
            SELECT *
            FROM reviews
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
   
 
   

    @classmethod
    def find_by_id(cls, review_id):
        """Return Review object corresponding to the table row matching the specified primary key."""
        sql = """
            SELECT * FROM reviews WHERE id = ?
        """
        row = CURSOR.execute(sql, (review_id,)).fetchone()
        return cls.instance_from_db(row) if row else None

   
    
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Review instances """
        sql = """
            CREATE TABLE IF NOT EXISTS reviews (
                id INTEGER PRIMARY KEY,
                username TEXT,
                comment TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                restaurant_id INTEGER,
                customer_id INTEGER,
                FOREIGN KEY (restaurant_id) REFERENCES restaurant(restaurant_id),
                FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS reviews;"
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = "INSERT INTO reviews (username, comment, restaurant_id, customer_id) VALUES (?, ?, ?, ?)"
        CURSOR.execute(sql, (self.username, self.comment, self.restaurant_id, self.customer_id))
        CONN.commit()
        self.review_id = CURSOR.lastrowid 
        type(self).all[self.review_id] = self

    @classmethod
    def create(cls, username, comment, restaurant_id, customer_id):
        review = cls(review_id=None, username=username, restaurant_id=restaurant_id, customer_id=customer_id, comment=comment, created_at=None)  
        review.save()
        return review
    
    
    

    
    # @classmethod
    # def create(cls, username, comment, restaurant_id, customer_id):
    #     # Verify foreign key references (assuming restaurant_id and customer_id are correct)
    #     restaurant_exists = CURSOR.execute(
    #         "SELECT 1 FROM restaurants WHERE restaurant_id = ?", (restaurant_id,)
    #     ).fetchone()
        
    #     if not restaurant_exists:
    #         raise ValueError("Error creating review: restaurant_id must reference a restaurant in the database.")
        
    #     customer_exists = CURSOR.execute(
    #         "SELECT 1 FROM customers WHERE customer_id = ?", (customer_id,)
    #     ).fetchone()
        
    #     if not customer_exists:
    #         raise ValueError("Error creating review: customer_id must reference a customer in the database.")
        
    #     # Insert the review
    #     sql = """
    #         INSERT INTO reviews (username, comment, restaurant_id, customer_id, created_at)
    #         VALUES (?, ?, ?, ?, datetime('now'))
    #     """
    #     CURSOR.execute(sql, (username, comment, restaurant_id, customer_id))
    #     CONN.commit()
        
    #     # Fetch the last inserted row
    #     review_id = CURSOR.lastrowid
    #     return cls.find_by_id(review_id)
    
  
    
    
    

    # def update(self):
    #     sql = "UPDATE reviews SET username = ?, comment = ?, restaurant_id = ?, customer_id = ? WHERE id = ?"
    #     CURSOR.execute(sql, (self.username, self.comment, self.restaurant_id, self.customer_id, self.review_id))
        # CONN.commit()


    def update(self):
        """Update the table row corresponding to the current Review instance."""
        sql = """
            UPDATE reviews
            SET username =?, comment =?, restaurant_id =?, customer_id =?
            WHERE id= ?
            
        """
        CURSOR.execute(sql, (self.username, self.comment, self.restaurant_id, self.customer_id,self.review_id))
        CONN.commit()



# UPDATE reviews(COLUMN 1, COL2) VALUES(?,?.?) WHERE id = ?
    
    
    def delete(self):
        sql = "DELETE FROM reviews WHERE id = ?"
        CURSOR.execute(sql, (self.review_id,))
        CONN.commit()
        del type(self).all[self.review_id]
        self.review_id = None





    # @classmethod
    # def instance_from_db(cls, row):
    #     """Return a Review object having the attribute values from the table row."""
        
    #     # Unpack row and check if instance already exists in `all` dictionary
    #     review_id, username, comment, created_at, restaurant_id, customer_id = row
    #     review = cls.all.get(review_id)
        
    #     if review:
    #         # Update any modified attributes if instance already exists
    #         review.username = username
    #         review.comment = comment
    #         review.created_at = created_at
    #         review.restaurant_id = restaurant_id
    #         review.customer_id = customer_id
    #     else:
    #         # Create a new instance if it doesn't exist in `all`
    #         review = cls(review_id, username, comment, created_at, restaurant_id, customer_id)
    #         cls.all[review_id] = review

    #     return review
    @classmethod
    def instance_from_db(cls, row):
        review_id, username, comment, created_at, restaurant_id, customer_id = row
        return cls(review_id=review_id, username=username, comment=comment, created_at=created_at, restaurant_id=restaurant_id, customer_id=customer_id)