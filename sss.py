import sqlite3
conn = sqlite3.connect('recipes.db')
cur = conn.cursor()
cur.execute('''CREATE TABLE recipes (name, cook_time, ingredients, difficulty)''')
recipes_data = [('Spaghetti Bolognese', '30 minutes', 'Pasta, Minced Meat, Tomato Sauce, Onion, Garlic', 3),
                ('Caesar Salad', '15 minutes', 'Lettuce, Chicken, Croutons, Parmesan Cheese, Caesar Dressing', 2),
                ('Chocolate Cake', '1 hour', 'Flour, Sugar, Eggs, Cocoa Powder, Butter, Baking Powder', 4)]
cur.executemany('INSERT INTO recipes VALUES (?,?,?,?)', recipes_data)
cur.execute('UPDATE recipes SET difficulty = 1 WHERE name = ?', ('Caesar Salad',))
cur.execute('DELETE FROM recipes WHERE name = ?', ('Chocolate Cake',))

for row in cur.execute('SELECT * FROM recipes'):
    print(row)
conn.commit()
conn.close()