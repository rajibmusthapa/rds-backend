from http.server import BaseHTTPRequestHandler
import json

PORTFOLIOS = [
    {"id": 1, "title": "E-Commerce Marketplace", "category": "Website", "client": "PT. Maju Jaya", "description": "Full Stack Web App dengan payment gateway"},
    {"id": 2, "title": "Company Profile Digital", "category": "Website", "client": "CV. Kreatif", "description": "Sistem manajemen proyek rating A+ security"},
    {"id": 3, "title": "Laundry Mobile App", "category": "Mobile App", "client": "Laundry Cepat", "description": "Aplikasi pesan antar laundry dengan tracking"}
]

def handler(request, context):
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'},
        'body': json.dumps(PORTFOLIOS)
    }
