lista = [{"country": "GB", "spent": 100}, {"country": "RU", "spent": 200}]
rjecnik = {}
for x in lista:
    rjecnik.update({x["country"]: x["spent"]})
print(rjecnik)