from database import database

def check_role(role_id: int):
    db = database.db
    # fetch current user role_id
    query = f"select role_power from role where role.role_id = {role_id}"
    print(query)
    res =  db.execute(query)
    a = res.fetchall()
    print(a)
    if a != []:
        for x in a:
            return x[0]
    else:
        return 'No User With Such Role'