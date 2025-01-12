import requests
import sys

zipcode = input("Enter your zide code:")
countrycode = input("Enter your country code:")
apikeys = "<apikeycode>"

weather_url = f"https://api.openweathermap.org/data/2.5/weather?zip={zip code},{country code}&appid={API key}"

result = requests.get(weather_url)

if result.status_code == 200:
  print(result.json())
  sys.exit(0)
else:
  print(f"ERROR: {result.json()['message']}")
  sys.exit(1)
