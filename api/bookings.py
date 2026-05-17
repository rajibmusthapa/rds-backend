import json
from datetime import datetime

# Simulasi database (nanti ganti dengan Supabase)
bookings_db = []

def handler(request, context):
    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type'
    }
    
    if request.method == 'OPTIONS':
        return {'statusCode': 204, 'headers': headers, 'body': ''}
    
    if request.method == 'GET':
        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps(bookings_db)
        }
    
    if request.method == 'POST':
        body = json.loads(request.body)
        body['id'] = len(bookings_db) + 1
        body['created_at'] = datetime.now().isoformat()
        body['status'] = 'pending'
        bookings_db.append(body)
        
        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps({'status': 'success', 'message': 'Booking terkirim!', 'data': body})
        }
    
    return {'statusCode': 405, 'headers': headers, 'body': json.dumps({'error': 'Method not allowed'})}
