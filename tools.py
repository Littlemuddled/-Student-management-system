import hashlib


def encrypt_password(passwd, x='qwertyuiopasdfghjklzxcvbnm'):
    h = hashlib.sha256()
    h.update(passwd.encode('utf8'))
    h.update(x.encode('utf8'))
    return h.hexdigest()
