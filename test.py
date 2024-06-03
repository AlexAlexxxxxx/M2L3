# import sqlite3 
# con = sqlite3.connect("kinopoisk.db") # соединение с базой данных, если бд нет, то файл создастся

# cur = con.cursor()
# ##cur.execute("CREATE TABLE movie(title, year, score)")
# # cur.execute("""
# #     INSERT INTO movie VALUES
# #         ('Monty Python and the Holy Grail', 1975, 8.2),
# #         ('And Now for Something Completely Different', 1971, 7.5),
# #         ('Men in black', 1997, 8.0)
# #         """)
# # con.commit()


# # for row in cur.execute("SELECT year, title FROM movie ORDER BY year"):
# #     print(row)

# t = cur.execute("SELECT title FROM movie ORDER BY score")
# for x in t:
#     print(x)
# con.close()

sp = (1, 4 ,2 ,4)
sp[0] = 123
print(sp)