from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from config import config

app = Flask(__name__)
connection = MySQL(app)

@app.route('/api/companies')
def get():
    cursor = connection.connection.cursor()
    cursor.execute("SELECT * FROM api_company")
    data = cursor.fetchall()
    
    companies = []
    for row in data:
        companies.append({
            'id': row[0],
            'name': row[1],
            'address': row[2],
            'city': row[3],
            'country': row[4],
        })
    return jsonify(companies)

@app.route('/api/companies/<int:id>')
def get_by_id(id):
    cursor = connection.connection.cursor()
    cursor.execute("SELECT * FROM api_company WHERE id = %s", (id,))
    data = cursor.fetchone()
    
    company = {
        'id': data[0],
        'name': data[1],
        'address': data[2],
        'city': data[3],
        'country': data[4],
    }
    return jsonify(company)

@app.route('/api/companies', methods=['POST'])
def post():
    cursor = connection.connection.cursor()
    cursor.execute("INSERT INTO api_company (name, city, country) VALUES (%s, %s, %s)", (request.json['name'], request.json['city'], request.json['country']))
    connection.connection.commit()
    return jsonify({'message': 'Company created successfully'})

@app.route('/api/companies/<int:id>', methods = ['PUT'])
def put(id):
    cursor = connection.connection.cursor()
    cursor.execute("UPDATE api_company SET name = %s, city = %s, country = %s WHERE id = %s", (request.json['name'], request.json['city'], request.json['country'], id))
    connection.connection.commit()
    return jsonify({'message': 'Company updated successfully'})

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()