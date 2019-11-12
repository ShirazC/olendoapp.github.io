import json

jsonFile =  open('setup.json')
jsonString = jsonFile.read()
jsonDate = json.loads(jsonString)


print(jsonDate['numPeople']["adults"])

jsonDate['UnRegion'] = "North America"

# print(jsonDate['UnRegion'])
# print(jsonDate)
