def city_country(city, country):
    #return city + "," + country
    return"{0}, {1}".format(city, country)

print(city_country("Montreal", " Quebec"))
print(city_country("Montreal", 123))