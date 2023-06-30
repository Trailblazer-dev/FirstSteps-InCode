import json
x = '{"name": "Daniel", "age":21,"IQ":"unknown"}'
y = json.loads(x)
#json.loads convert js built data types to python
print(y)
i = {
    "ocean": "pacific",
    "ship": "cruise"
}
print(json.dumps(i))
# json.dumps convert python built data to javascript
