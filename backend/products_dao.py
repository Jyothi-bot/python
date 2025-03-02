from sql_connection import get_sql_connection
def get_all_products(connection):
    cursor = connection.cursor()
    query = ("select products.product_id, products.name,\
          products.unit_id, products.price_per_unit,\
          unit.unit_name\
          from products inner join unit on\
          products.unit_id=unit.unit_id")
    cursor.execute(query)
    response = []
    #rows = cursor.fetchall()
    for (product_id, name, unit_id, price_per_unit, unit_name) in cursor:
        response.append({
                'product_id' : product_id,
                'name' : name,
                'unit_id' : unit_id,
                'price_per_unit': price_per_unit,
                'unit_name' : unit_name
            })  
    return response
def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("insert into products"
            " (name, unit_id, price_per_unit)"
             " values (%s, %s, %s)")
    data = (product['product_name'], product['unit_id'], product['price_per_unit'])
    cursor.execute(query, data)
    connection.commit()
    return cursor.lastrowid
def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM products where product_id=" + str(product_id))
    cursor.execute(query)
    connection.commit()



if __name__ =='__main__':
    connection = get_sql_connection()
    print(delete_product(connection, 8))
    print(insert_new_product(connection, {
        'product_name' : 'potato',
        'unit_id' : '1',
        'price_per_unit' : '20'
    }))
        