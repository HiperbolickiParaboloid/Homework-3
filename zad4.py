import json
with open("zad4.json", "r", encoding="utf-8") as json_file:
    content = json.load(json_file)
    for element in content["flight_data"]["outgoing"]:
        if "layover" in element.keys():
            del element["layover"]
        elif "from" in element.keys():
            del element["from"]["timestamp"]
            del element["from"]["timestamp_utc"]
        elif "to" in element.keys():
            del element["to"]["timestamp"]
            del element["to"]["timestamp_utc"]
    del content["passenger_data"][0]["final_date"]
    del content["passenger_data"][0]["adult_ind"]
    del content["passenger_data"][0]["_type"]
    del content["_price_change"]
    del content["keep_alive"]

json_name = content["flight_data"]["info"]["route"]
json_name_lower = json_name.lower()
city_names = json_name_lower.split("|")
final_city_names = []
for city in city_names:
    final_city_names.append(city.replace(" ","_"))
new_json_name = final_city_names[0] + "_" + final_city_names[1] + ".json"

with open(new_json_name, 'w', encoding="utf-8") as json_file:
    content = json.dump(content, json_file)