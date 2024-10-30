from models.__init__ import CURSOR, CONN

class Customer:
    all = {}
#Initialize a Customer instance with name, body
    def __init__(self, name, body, id=None):
        self.id = id
        self.name = name
        self.body = body

    def __repr__(self): #Return a string representation of the Customer instance.
        return f"<Customer {self.id}: {self.name}>"

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
    def body(self):
        return self._body

    @body.setter
    def body(self, value):
        if isinstance(value, str):
            self._body = value
        else:
            raise ValueError("Body must be a string")

    @classmethod
    def create_table(cls): # Create the customers table if it does not already exist.
        sql = """
            CREATE TABLE IF NOT EXISTS customers (
                customer_id INTEGER PRIMARY KEY,
                name TEXT,
                body TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def get_all(cls): #Retrieve all customers from the database and return as a list of Customer instances.
        """Return a list containing a customer object per row in the table"""
        sql = """
            SELECT *
            FROM customers
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

     
    @classmethod
    def drop_table(cls): #Drop the customers table if it exists.
        sql = "DROP TABLE IF EXISTS customers;"
        CURSOR.execute(sql)
        CONN.commit()

    def save(self): #Insert a new row into the database for this Customer instance and update its id.
        """ Insert a new row with the name and body values of the current Customer instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO customers (name, body)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.body))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
        
        
    @classmethod
    def find_by_id(cls, customer_id):       #Find a Customer instance by ID and return it.
        """Return a Customer object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM customers
            WHERE customer_id = ?
        """

        row = CURSOR.execute(sql, (customer_id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name): #Find a Customer instance by name and return the first match.
        """Return a Customer object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM customers
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def create(cls, name, body):   #   Create a new Customer instance and save it to the database.
        customer = cls(name, body)
        customer.save()
        return customer
    

    def update(self):  #Update the database entry for this Customer instance.
        sql = "UPDATE customers SET name = ?, body = ? WHERE customer_id = ?"
        CURSOR.execute(sql, (self.name, self.body, self.id))
        CONN.commit()

    def delete(self):   #Delete the database entry for this Customer instance.
        sql = "DELETE FROM customers WHERE customer_id = ?"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):   #Create a Customer instance from a database row.
        customer_id, name, body = row
        return cls(id=customer_id, name=name, body=body)