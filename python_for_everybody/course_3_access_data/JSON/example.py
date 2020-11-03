import json

data = '''
{
    "name" : "Alex",
    "phone" : {
        "type" : "intl",
        "number" : "+1 123 123 3344"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

info = json.loads(data)
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])