from jose import jwt

SECRET_KEY = '6470010fd1b67d9d36d9e9d3b663864849e17d0f18c12260774c99a271759c1f'

def create_token(tok: dict):
    to_encode = tok.copy()
    token = jwt.encode(to_encode,SECRET_KEY)
    return token

def decode_token(token: str):
    return(jwt.decode(token,SECRET_KEY))