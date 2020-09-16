import json

data = '''
[
{
"name": "Kaileb",
"count": 98
},
{
"name": "Mykie",
"count": 97
},
{
"name": "Grayson",
"count": 95
},
{
"name": "Kassia",
"count": 94
},
{
"name": "Ashleigh",
"count": 93
},
{
"name": "Hayleigh",
"count": 91
},
{
"name": "Khalida",
"count": 90
},
{
"name": "Will",
"count": 83
},
{
"name": "Charley",
"count": 83
},
{
"name": "Labhaoise",
"count": 83
},
{
"name": "Nadine",
"count": 74
},
{
"name": "Bilal",
"count": 72
},
{
"name": "Meerab",
"count": 70
},
{
"name": "Caleb",
"count": 68
},
{
"name": "Aryan",
"count": 64
},
{
"name": "Bezalel",
"count": 62
},
{
"name": "Mirryn",
"count": 61
},
{
"name": "Zohaib",
"count": 58
},
{
"name": "Eireyn",
"count": 58
},
{
"name": "Ahmad",
"count": 56
},
{
"name": "Gemima",
"count": 55
},
{
"name": "Brigitte",
"count": 51
},
{
"name": "Mckenzie",
"count": 50
},
{
"name": "Vincenzo",
"count": 49
},
{
"name": "Meili",
"count": 49
},
{
"name": "Danna",
"count": 49
},
{
"name": "Faizaan",
"count": 48
},
{
"name": "Avsta",
"count": 45
},
{
"name": "Vaila",
"count": 45
},
{
"name": "Manolo",
"count": 45
},
{
"name": "Valentina",
"count": 41
},
{
"name": "Clea",
"count": 34
},
{
"name": "Lilliarna",
"count": 34
},
{
"name": "Tanzina",
"count": 34
},
{
"name": "Aisha",
"count": 33
},
{
"name": "Lillie",
"count": 24
},
{
"name": "Mustapha",
"count": 24
},
{
"name": "Sheanne",
"count": 18
},
{
"name": "Truli",
"count": 16
},
{
"name": "Lorraine",
"count": 16
},
{
"name": "Orlanna",
"count": 16
},
{
"name": "Carmel",
"count": 12
},
{
"name": "Tiana",
"count": 11
},
{
"name": "Arfa",
"count": 10
},
{
"name": "Keegan",
"count": 9
},
{
"name": "Aisa",
"count": 7
},
{
"name": "Saman",
"count": 6
},
{
"name": "Rupert",
"count": 5
},
{
"name": "Malo",
"count": 4
},
{
"name": "Zubayr",
"count": 2
}
]'''

info = json.loads(data)
print('User count:', len(info))

sum = 0
for item in info:
    sum = sum + int(item['count'])
print(sum)
