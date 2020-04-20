import requests

print('''\033[34;1m
   __  ___          ____                          
  /  |/  /__ ____  / __/______ ____  ___  ___ ____
 / /|_/ / _ `/ _ \_\ \/ __/ _ `/ _ \/ _ \/ -_) __/
/_/  /_/\_,_/ .__/___/\__/\_,_/_//_/_//_/\__/_/   
           /_/                                    
            -- Coded by Md Saikat                               
\033[0m''')
api =input("Enter your api key~") 
r = requests.get("https://www.google.com/maps/embed/v1/place?q=place_id:ChIJyX7muQw8tokR2Vf5WBBk1iQ&key="+api)
if r.status_code == 200:
    print("\033[0;32;1mGreen Vulnerable  Embed")
else:
    print("\033[0;31;1mNot Vulnerable  Embed")     
r =requests.get("https://maps.googleapis.com/maps/api/streetview?size=400x400&location=40.720032,-73.988354&fov=90&heading=235&pitch=10&key="+api)
if r.status_code == 200:
    print("\033[0;32;1mGreen Vulnerable  Street View API")
else:
    print('\033[0;31;1mNot Vulnerable  Street View API')
r = requests.get("https://maps.googleapis.com/maps/api/directions/json?origin=Disneyland&destination=Universal+Studios+Hollywood4&key="+api)
if r.status_code == 200:
    print("\033[0;32;1mGreen Vulnerable  Directions API")
else:
    print('\033[0;31;1mNot Vulnerable  Directions API')
r = requests.get("https://maps.googleapis.com/maps/api/geocode/json?latlng=40,30&key="+api)
if r.status_code == 200:
    print("\033[0;32;1mGreen Vulnerable  Gecoding API")
else:
    print('\033[0;31;1mNot Vulnerable  Gecoding API')
r = requests.get("https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=40.6655101,-73.89188969999998&destinations=40.6905615%2C-73.9976592%7C40.6905615%2C-73.9976592%7C40.6905615%2C-73.9976592%7C40.6905615%2C-73.9976592%7C40.6905615%2C-73.9976592%7C40.6905615%2C-73.9976592%7C40.659569%2C-73.933783%7C40.729029%2C-73.851524%7C40.6860072%2C-73.6334271%7C40.598566%2C-73.7527626%7C40.659569%2C-73.933783%7C40.729029%2C-73.851524%7C40.6860072%2C-73.6334271%7C40.598566%2C-73.7527626&key="+api)
if r.status_code == 200:
    print("\033[0;32;1mGreen Vulnerable  Distance matrix API")
else:
    print('\033[0;31;1mNot Vulnerable  Distance matrix API')
r = requests.get("https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=Museum%20of%20Contemporary%20Art%20Australia&inputtype=textquery&fields=photos,matted_address,name,rating,opening_hours,geometry&key="+api)
if r.status_code == 200:
    print("\033[0;32;1mGreen Vulnerable  Findplace from text API")
else:
    print('\033[0;31;1mNot Vulnerable Findplace from text API')
r = requests.get("https://maps.googleapis.com/maps/api/place/autocomplete/json?input=Bingh&types=%28cities%29&key="+api)
if r.status_code == 200:
    print("\033[0;32;1mGreen Vulnerable  Autocomplete API")
else:
    print('\033[0;31;1mNot Vulnerable  Autocomplete API')
r = requests.get("https://maps.googleapis.com/maps/api/elevation/json?locations=39.7391536,-104.9847034&key="+api)
if r.status_code == 200:
    print("\033[0;32;1mGreen Vulnerable  Elevation API")
else:
    print('\033[0;31;1mNot Vulnerable  Elevation API')
r = requests.get("https://maps.googleapis.com/maps/api/timezone/json?location=39.6034810,-119.6822510&timestamp=1331161200&key="+api)
if r.status_code == 200:
    print("\033[0;32;1mGreen Vulnerable  Timezone API")
else:
    print('\033[0;31;1mNot Vulnerable  Timezone API')
r = requests.get("https://roads.googleapis.com/v1/nearestRoads?points=60.170880,24.942795|60.170879,24.942796|60.170877,24.942796&key="+api)
if r.status_code == 200:
    print("\033[0;32;1mGreen Vulnerable  Roads API")
else:
    print('\033[0;31;1mNot Vulnerable  Roads API')
r = requests.get("https://www.googleapis.com/geolocation/v1/geolocate?key="+api)
if r.status_code == 200:
    print("\033[0;32;1mGreen Vulnerable  Geolocation API")
else:
    print('\033[0;31;1mNot Vulnerable  Geolocation API')