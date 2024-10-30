from models.__init__ import CURSOR, CONN

class Restaurant:
    all = {}

    def __init__(self, name, address, rating, restaurant_id=None):
        self.restaurant_id = restaurant_id
        self.name = name
        self.address = address
        self.rating = rating
        if restaurant_id is not None:
            Restaurant.all[restaurant_id] = self

    def __repr__(self):
        return f"<Restaurant {self.restaurant_id}: {self.name}>"
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and value:
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string")

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        if isinstance(value, str) and value:
            self._address = value
        else:
            raise ValueError("Address must be a non-empty string")

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        if isinstance(value, str) and value.replace(".", "").isdigit():
            self._rating = value
        else:
            raise ValueError("Rating must be a valid numeric string")
        
    @classmethod
    def get_all(cls):
        """Return a list containing a Restaurants object per row in the table"""
        sql = """
            SELECT *
            FROM restaurants
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def create_table(cls):
        sql = """
        CREATE TABLE IF NOT EXISTS restaurants (
            restaurant_id INTEGER PRIMARY KEY,
            name TEXT,
            address TEXT,
            rating TEXT
        )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS restaurants;" 
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the restaurant name, address, and rating  values of the current restaurant object.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
                INSERT INTO restaurants (name, address, rating)
                VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.address, self.rating))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
        
    @classmethod
    def create(cls, name, address, rating):
        restaurant = cls(name=name, address=address, rating=rating)
        restaurant.save()
        return restaurant

    def update(self):
        sql = "UPDATE restaurants SET name = ?, address = ?, rating = ? WHERE restaurant_id = ?"
        CURSOR.execute(sql, (self.name, self.address, self.rating, self.restaurant_id))
        CONN.commit()

    def delete(self):
        sql = "DELETE FROM restaurants WHERE restaurant_id = ?"
        CURSOR.execute(sql, (self.restaurant_id,))
        CONN.commit()
        del type(self).all[self.restaurant_id]
        self.restaurant_id = None

    @classmethod
    def find_by_name(cls, name):
        sql = "SELECT * FROM restaurants WHERE name = ?"
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None    

    # @classmethod
    # def instance_from_db(cls, row):
    #     restaurant_id, name, address, rating = row
    #     return cls(name=name, address=address, rating=rating, restaurant_id=restaurant_id)

    

    @classmethod
    def find_by_id(cls, id_):
        sql = "SELECT * FROM restaurants WHERE restaurant_id = ?"
        row = CURSOR.execute(sql, (id_,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def instance_from_db(cls, row):
        restaurant_id, name, address, rating = row
        return cls(name=name, address=address, rating=rating, restaurant_id=restaurant_id)