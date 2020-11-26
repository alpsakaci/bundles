from Crypto.Cipher import AES
from base64 import b64encode, b64decode
from Crypto.Util.Padding import pad, unpad
import secretpass.settings as settings

def encrypt_password(password):
    data = bytes(password, encoding="utf-8")
    key_str = settings.SP_PASSPHRASE
    key = bytes(key_str, encoding="utf-8")
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    iv = b64encode(cipher.iv).decode("utf-8")
    ct = b64encode(ct_bytes).decode("utf-8")
    
    return iv + ct
    

def decrypt_password(password):
    try:
        iv = b64decode(password[:24])
        ct = b64decode(password[24:])
        key_str = settings.SP_PASSPHRASE
        key = bytes(key_str, encoding="utf-8")
        cipher = AES.new(key, AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), AES.block_size)
        return pt
    except:
        return None
