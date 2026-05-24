import pymysql
import os



config = {
    'host': 'ich-db.edu.itcareerhub.de',
    'user': 'ich1',
    'password': 'password',
    'database': 'world',
}

conn = pymysql.connect(**config)
cursor = conn.cursor()

cursor.execute('SELECT Name FROM country')
countries = cursor.fetchall()

for num, country in enumerate(countries, 1):
    print(f"{num}. {country[0]}")


user_country = input("Enter your country code or name: ")
if user_country.isdigit():
    country_name = countries[int(user_country) - 1][0]
else:
    country_name = user_country


for num, country in enumerate(cursor.fetchall(), 1):
    if user_country == num:
        user_country = country[0]

cursor.execute('SELECT Code FROM country WHERE Name = %s', (country_name,))
country_code = cursor.fetchone()
cursor.execute('SELECT Name, Population FROM city WHERE CountryCode = %s', (country_code,))
for num, city in enumerate(cursor.fetchall(), 1):
    print(f"{num}. {city[0]} - {city[1]}")

cursor.close()
conn.close()