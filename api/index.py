from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
import json
import hashlib

app = Flask(__name__)
CORS(app)

# Database Sementara (akan hilang jika server restart)
bookings_db = []

@app.route('/api/products', methods=['GET'])
def get_products():
    products = {
        "1": {"id": "1", "name": "Web Development", "price_min": 8000000, "price_max": 75000000, "description": "Website profesional, company profile, marketplace, e-commerce, dan CMS modern.", "icon": "💻"},
        "2": {"id": "2", "name": "Mobile App Development", "price_min": 15000000, "price_max": 150000000, "description": "Aplikasi iOS & Android native dan cross-platform dengan UI/UX modern.", "icon": "📱"},
        "3": {"id": "3", "name": "Cyber Security", "price_min": 10000000, "price_max": 85000000, "description": "Perlindungan aset digital perusahaan dari ancaman siber.", "icon": "🔒"}
    }
    return jsonify(products)

@app.route('/api/bookings', methods=['GET', 'POST'])
def handle_bookings():
    if request.method == 'GET':
        return jsonify(bookings_db)
    
    if request.method == 'POST':
        data = request.json
        data['id'] = len(bookings_db) + 1
        data['created_at'] = datetime.now().isoformat()
        data['status'] = 'pending'
        bookings_db.append(data)
        return jsonify({'status': 'success', 'message': 'Booking terkirim!', 'data': data})

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    password = data.get('password', '')
    # Gunakan hashing yang lebih aman di production
    if password == 'admin123':
        token = hashlib.sha256(f"{datetime.now()}{password}".encode()).hexdigest()
        return jsonify({'status': 'success', 'token': token})
    return jsonify({'status': 'error', 'message': 'Password salah'}), 401

@app.route('/api/portfolio', methods=['GET'])
def get_portfolio():
    portfolios = [
        {"id": 1, "title": "E-Commerce Marketplace", "category": "Website", "client": "PT. Maju Jaya", "description": "Full Stack Web App dengan payment gateway"},
        {"id": 2, "title": "Company Profile Digital", "category": "Website", "client": "CV. Kreatif", "description": "Sistem manajemen proyek rating A+ security"},
        {"id": 3, "title": "Laundry Mobile App", "category": "Mobile App", "client": "Laundry Cepat", "description": "Aplikasi pesan antar laundry dengan tracking"}
    ]
    return jsonify(portfolios)

@app.route('/api/testimonials', methods=['GET'])
def get_testimonials():
    testimonials = [
        {"id": 1, "name": "Donwahab Pool", "message": "Kami kasih rating 6/6 untuk layanan RDS. Website yang dibuat simpel, rapi, dan mudah diakses lewat HP.", "rating": 5},
        {"id": 2, "name": "Enjang Rahman", "message": "Sangat bagus 👍", "rating": 5},
        {"id": 3, "name": "Mio Soul", "message": "Mantap trimakasi ❤️", "rating": 5}
    ]
    return jsonify(testimonials)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
