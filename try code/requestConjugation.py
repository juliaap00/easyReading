# importing the requests library
import requests

# api-endpoint
URL = "https://conjugador.reverso.net/conjugacion-espanol-verbo-abolir.html"

# location given here


# sending get request and saving the response as response object
r = requests.get(url = URL)

# extracting data in json format
print(r.headers)


# extracting latitude, longitude and formatted address
# of the first matching location
