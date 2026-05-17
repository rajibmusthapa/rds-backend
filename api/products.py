import json

PRODUCTS = {
    "1": {"id": "1", "name": "Web Development", "price_min": 8000000, "price_max": 75000000, "description": "Website profesional, company profile, marketplace, e-commerce, dan CMS modern.", "icon": "💻"},
    "2": {"id": "2", "name": "Mobile App Development", "price_min": 15000000, "price_max": 150000000, "description": "Aplikasi iOS & Android native dan cross-platform dengan UI/UX modern.", "icon": "📱"},
    "3": {"id": "3", "name": "Cyber Security", "price_min": 10000000, "price_max": 85000000, "description": "Perlindungan aset digital perusahaan dari ancaman siber.", "icon": "🔒"}
}

def handler(request, context):
    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
    }
    
    return {
        'statusCode': 200,
        'headers': headers,
        'body': json.dumps(PRODUCTS)
    }
