from connections import connection
def explorer(obj, db):
    con = connection.new_connection("adonais1_tickets_0")
    con1 = connection.new_connection(db)
    filters = obj.get("filters")
    paging = obj.get("paging")
    order = obj.get("orders")
    route = obj("router")

    cursor = con.cursor()
    cursor.execute(f"select sql from dynamic where route = {route}")
