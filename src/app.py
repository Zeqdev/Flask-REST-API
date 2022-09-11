from flask import Flask, jsonify
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

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()