class Location:
    default_country = "brazil"

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def get(self):
        print(f"Latitude ({self.latitude}) - Longitude ({self.longitude})")

Location.default_country = "EUA"
location = Location(12312, 321312)
print(Location.default_country)
print(location.default_country)