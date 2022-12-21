sampleDict = { 
  "name": "Avinash",
  "age":45, 
  "salary": 98000, 
  "city": "London" }

keys = ["name", "salary"]

newDict = {k: sampleDict[k] for k in keys}
print(newDict)