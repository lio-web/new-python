from models.__init__ import CURSOR, CONN

class Customer:
    all = {}

    def __init__(self, name, body, id=None):
        self.id = id
        self.name = name
        self.body = body

    def __repr__(self):
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
    def create_table(cls):
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
    def get_all(cls):
        """Return a list containing a customer object per row in the table"""
        sql = """
            SELECT *
            FROM customers
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    
    # @classmethod
    # def get_all(cls):
    #     sql = "SELECT * FROM customers"
    #     rows = CURSOR.execute(sql).fetchall()
    #     cls.all.clear()  # Clear the current cache
    #     customers = [cls.instance_from_db(row) for row in rows] if rows else []
    #     for customer in customers:
    #      cls.all[customer.id] = customer  # Cache the customers
    #     return customers



     
    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS customers;"
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
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
    def find_by_id(cls, customer_id):
        """Return a Customer object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM customers
            WHERE customer_id = ?
        """

        row = CURSOR.execute(sql, (customer_id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """Return a Customer object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM customers
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def create(cls, name, body):
        customer = cls(name, body)
        customer.save()
        return customer
    

    def update(self):
        sql = "UPDATE customers SET name = ?, body = ? WHERE customer_id = ?"
        CURSOR.execute(sql, (self.name, self.body, self.id))
        CONN.commit()

    def delete(self):
        sql = "DELETE FROM customers WHERE customer_id = ?"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        customer_id, name, body = row
        return cls(id=customer_id, name=name, body=body)