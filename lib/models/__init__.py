import sqlite3

CONN = sqlite3.connect('restaurant_management.db')
CURSOR = CONN.cursor()
