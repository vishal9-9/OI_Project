from werkzeug.security import generate_password_hash,check_password_hash

def hash(password: str):
    return(generate_password_hash(password))
 
def unhash(hpass: str, upass: str):
    return(check_password_hash(hpass,upass))