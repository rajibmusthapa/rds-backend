import json
import hashlib
from datetime import datetime

def handler(request, context):
    if request.method == 'POST':
        body = json.loads(request.body)
        password = body.get('password', '')
        
        # Hash password (ganti dengan hash yang aman)
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        admin_hash = hashlib.sha256("admin123".encode()).hexdigest()
        
        if password_hash == admin_hash:
            token = hashlib.sha256(f"{datetime.now()}{password}".encode()).hexdigest()
            return {
                'statusCode': 200,
                'headers': {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'},
                'body': json.dumps({'status': 'success', 'token': token})
            }
    
    return {
        'statusCode': 401,
        'headers': {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'},
        'body': json.dumps({'status': 'error', 'message': 'Unauthorized'})
    }
