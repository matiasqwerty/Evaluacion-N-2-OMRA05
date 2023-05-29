import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key= "IjF37u0pDNyLSoBUwFU67GBDxd3d8eR6"

while True:
    orig = input("ciudad de Origen")
    if orig=="q":
        break
    dest = input("Ciudad de destino")
    if dest =="q":
        break
    url = main_api + urllib.parse.urlencode({"key": key, "from": orig, "to": dest})
    print("URL: " + url)
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print("=============================================")
        print("El viaje de " + orig + " a " + dest)
        print("Tomo : " + json_data["route"]["formattedTime"],"Hrs y acumulo un ")
        distance = json_data["route"]["distance"]
        rounded_distance = round(distance, 2)
        print("Total de " + str(rounded_distance),"kilometros recorridos ")
        print("=============================================")