import requests, pprint

postalcode = input("Código Postal: ")
url = f"https://api.zippopotam.us/es/{postalcode}"

headers = {
    "Content-Type": "application/json",
    "X-Client-Id": "demo-demo-demo"
}

try:
    response = requests.request("get", url, headers=headers)
    response = requests.get(url, headers=headers)

    if(response.status_code == 200):
        datos = response.text
        data = response.json()

        # print(f"Datos: {datos}")
        # print(type(datos))
        # print("")
        # print(f"Data: {data}")
        # print(type(data))

        print(f"Información para {data["post code"]} {data["country"]}")
        for item in data["places"]:
            print(f" |-> {item["place name"]} - {item["state"]}")
    else:
        print(f"Error ({response.status_code}): {response.reason}")

except Exception as err:
    print (f"Error: {err}")