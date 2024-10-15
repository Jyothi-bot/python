from flask import Flask, request, jsonify
import products_dao
import unit_dao
from sql_connection import get_sql_connection
app = Flask(__name__)
connection = get_sql_connection()
@app.route('/getProducts', methods=['GET'])
def get_products():
    products = products_dao.get_all_products(connection)
    response = jsonify(products) 
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
@app.route('/getunit', methods=['GET'])
def get_unit():
    response = unit_dao.get_unit(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
@app.route('/getProducts', methods=['POST'])
def delete_products():
    return_id = products_dao.delete_product(connection, request.form['product_id'])
    response = jsonify({
        'product_id' : return_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

    #return "Hello, how are you"


if __name__ == "__main__":
    print("Starting Python Flask Server For Grocery Store Management System")
    app.run(port=5000)