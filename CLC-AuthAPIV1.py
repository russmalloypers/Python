import requests
import json
url = "https://api.ctl.io/v2/servers/ssbe/UC1SSBEAPM10304"

headers = {
    'content-type': 'application/json',
    'authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ1cm46YXBpLXRpZXIzIiwiYXVkIjoidXJuOnRpZXIzLXVzZXJzIiwibmJmIjoxNTI4MjUxNzAxLCJleHAiOjE1Mjk0NjEzMDEsInVuaXF1ZV9uYW1lIjoicnVzcy5tYWxsb3kiLCJ1cm46dGllcjM6YWNjb3VudC1hbGlhcyI6IlQzTiIsInVybjp0aWVyMzpsb2NhdGlvbi1hbGlhcyI6IldBMSIsInJvbGUiOiJBZG1pbmlzdHJhdG9yIn0.xlE38APefESx1W83ef3L-0k7KsfPxXBsjDW_Fu53NGo",
    'cache-control': 'no-cache',
    'postman-token': '7b66c692-6906-fa43-c0a4-4b5a34859d5c'
}

r = requests.request("GET", url, headers=headers)
print(r.json())

