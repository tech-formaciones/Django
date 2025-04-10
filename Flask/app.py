from flask import Flask, request, Response, redirect, jsonify, abort
from flask_sqlalchemy import SQLAlchemy

app =  Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = ('mssql+pyodbc://dbuser:demo@localhost/northwind?driver=ODBC+Driver+17+for+SQL+Server')

db = SQLAlchemy(app)

class Customer(db.Model):
    __tablename__ = 'Customers'
    customerid =  db.Column(db.String(5), primary_key=True)
    companyname =  db.Column(db.String(40), nullable=False)
    contactname =  db.Column(db.String(30))
    contacttitle =  db.Column(db.String(30))
    address =  db.Column(db.String(60))
    city =  db.Column(db.String(15))
    region =  db.Column(db.String(15))
    postalcode =  db.Column(db.String(10))
    country =  db.Column(db.String(15))
    phone =  db.Column(db.String(24))
    fax =  db.Column(db.String(24))

    def to_dict(self):
        return {
            'customerid': self.customerid,
            'companyname': self.companyname,
            'contactname': self.contactname,
            'contacttitle':  self.contacttitle,
            'address':  self.address,
            'city':  self.city,
            'region':  self.region,
            'postalcode':  self.postalcode,
            'country':  self.country,
            'phone':  self.phone,
            'fax':  self.fax,
        }

#########################################################

# API Key Middleware
# curl -X GET "http://127.0.0.1:5000/customers" -H "X-API-KEY: 123456secret"

API_KEY = "123456secret"

@app.before_request
def require_api_key():
    if request.endpoint != 'public_route':
        key = request.headers.get('X-API-KEY')
        if key != API_KEY:
            abort(401, description="Invalid or missing API Key")

#########################################################

@app.route('/customers', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    return jsonify([c.to_dict() for c in customers])

@app.route('/customers/<customer_id>', methods=['GET'])
def get_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    return jsonify({k: v for k,v in customer.__dict__.items() if k != '_sa_instance_state'})

@app.route('/customers', methods=['POST'])
def create_customer():
    data = request.json
    customer = Customer(**data)
    db.session.add(customer)
    db.session.commit()
    return jsonify({'message': 'Customer created'}), 201

@app.route('/customers/<customer_id>', methods=['PUT'])
def update_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    data = request.json
    for key, value in data.items():
        setattr(customer, key, value)
    db.session.commit()
    return jsonify({'message': 'Customer updated'})

@app.route('/customers/<customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    db.session.delete(customer)
    db.session.commit()
    return jsonify({'message': 'Customer deleted'})


if __name__ == '__main__':
    app.run(debug=True)