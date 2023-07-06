import urllib.parse
import requests

main_api = "https://mapquestapi.com/directions/v2/route?"
key = "e4bFZLKnXeV6gF1LhdwmrSzHCQfsg0fd"

while True:
   orig = input("Ciudad de Origen: ")
   if orig == "quit" or orig == "s":
       break
   dest = input("Destino: ")
   if dest == "quit" or dest == "s":
       break 
   url = main_api + urllib.parse.urlencode({"key":key,"from":orig,"to":dest})
   json_data = requests.get(url).json()

   print("URL: " + (url))

   json_data = requests.get(url).json()
   json_status = json_data["info"]["statuscode"]

   if json_status == 0:
       print("API Status: " + str(json_status) + " = A successful route call.\n")
       print("=============================================")
       print("Directions from " + (orig) + " to " + (dest))
       print("Trip Duration:   " + (json_data["route"]["formattedTime"]))
       print("Kilometers:      " + str("{:.1f}".format((json_data["route"]["distance"])*1.61)))
       print("=============================================")
       for each in json_data["route"]["legs"][0]["maneuvers"]:
           print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
       print("=============================================\n")


          

       
       













 