import sqlite3
 
with sqlite3.connect("top_hotels.db") as db:

      cursor=db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS hotels(

id integer PRIMARY KEY,
hotel text NOT NULL,
location text NOT NULL,
country text NOT NULL,
region text NOT NULL,
company text NOT NULL,
score real NOT NULL,
rank integer NOT NULL,
rooms integer NOT NULL,
theme text NOT NULL,
year integer NOT NULL);
""")
# top_hotels = open("top_hotels.csv", "r")
# for line in top_hotels:
#     contents = line.split(",")
#     #print(contents)
#     cursor.execute("""INSERT INTO hotels(hotel, location, country, region, company, score, rank, rooms, theme, year)
#     VALUES (?,?,?,?,?,?,?,?,?,?) """, (contents[0], contents[1], contents[2], contents[3], contents[4], contents[5], contents[6], contents[7], contents[8], contents[9]))
#     db.commit()
 
# for row in cursor.execute('SELECT * FROM hotels'):
#         print(row)
complete=cursor.execute('select*from hotels')

# newID = int(input("Enter ID number: "))
# location = input("Enter the location: ")
# company = input("Enter the company: ")
# score = float(input("Enter a score: "))
# rank = input("Enter the rank: ")
# theme = input("Enter a theme: ")
# year = int(input("Enter a year: "))
fill = input("Do you want to filter your search by: Hotel, Country, Region, Rank or Room number: ")
 
if fill == "Hotel":
    hotel_name = input("Enter the name of the hotel: ")
    for entry in complete:
        if hotel_name in entry:
            print(entry)
 
elif fill == "Country":
    country_name = input("Enter the country: ")
    for entry in complete:
        if country_name in entry:
            print(entry)
 
elif fill == "Region":
    region_name = input("Enter the region: ")
    for entry in complete:
        if region_name in entry:
            print(entry)
 
elif fill == "Rank":
    min_rank = int(input("Enter a minimum rank: "))
    max_rank = int(input("Enter a maximum rank: "))
    for entry in complete:
#         print(entry[7])
        if str(entry[7]).isdigit() and int(entry[7]) >= min_rank and int(entry[7]) <= max_rank:
            print(entry)
 
else:
    room_num = int(input("Enter the minimum amount of rooms needed: "))
    for entry in complete:
        if room_num in entry:
            print(entry)
 
# db.commit()
# hotel_name = input("Enter the name of the hotel: ")
# if hotel_name == hotel:
#     print(hotel_name, "is in the database")
# 
# else:
#     print("That hotel was not found in the database.")
#  
# country_name = input("Enter the country: ")
# if country_name == country:
#     print(country_name, "is in the database")
# else:
#     print("That country was not found in the database.")
# region_name = input("Enter the region: ")
# if region_name == region:
#     print(region_name, "is in the database")
# else:
#     print("That region was not found in the database.")
# room_num = int(input("Enter the minimum amount of rooms needed: "))
# 
# if room_num == rooms:
#     print("we have a hotel with", rooms, "rooms in tht database")
# else:
#     print("That country was not found in the database.")
 


 