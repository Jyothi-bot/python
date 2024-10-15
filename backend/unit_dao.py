def get_unit(connection):
    cursor = connection.cursor()
    query = ("SELECT * from unit")
    cursor.execute(query)
    response = []
    for(unit_id, unit_name) in cursor:
        response.append({
            'unit_id' : unit_id,
            'unit_name' : unit_name
		})
if __name__ == '__main__':
    from sql_connection import get_sql_connection_cursor
    connection = get_sql_connection_cursor()
    print(get_unit(connection))