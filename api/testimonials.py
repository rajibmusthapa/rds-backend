from http.server import BaseHTTPRequestHandler
import json

TESTIMONIALS = [
    {"id": 1, "name": "Donwahab Pool", "message": "Kami kasih rating 6/6 untuk layanan RDS.", "rating": 5},
    {"id": 2, "name": "Enjang Rahman", "message": "Sangat bagus 👍", "rating": 5},
    {"id": 3, "name": "Mio Soul", "message": "Mantap trimakasi ❤️", "rating": 5}
]

def handler(request, context):
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'},
        'body': json.dumps(TESTIMONIALS)
    }
