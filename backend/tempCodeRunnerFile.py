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

if __name__ =='__main__':
    connection = get_sql_connection()
    print(get_all_products(connection))
        