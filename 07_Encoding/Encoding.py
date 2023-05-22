import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend

def generate_key(password, salt):
    password_bytes = password.encode('utf-8')
    salt_bytes = salt.encode('utf-8')
    
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt_bytes,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password_bytes))
    
    return key

def encrypt_file(file_path, output_file_path, password, salt):
    with open(file_path, 'rb') as file:
        file_content = file.read()
    
    key = generate_key(password, salt)
    cipher_suite = Fernet(key)
    encrypted_content = cipher_suite.encrypt(file_content)
    
    with open(output_file_path, 'wb') as output_file:
        output_file.write(encrypted_content)

def decrypt_file(file_path, output_file_path, password, salt):
    with open(file_path, 'rb') as file:
        file_content = file.read()
    
    key = generate_key(password, salt)
    cipher_suite = Fernet(key)
    decrypted_content = cipher_suite.decrypt(file_content)
    
    with open(output_file_path, 'wb') as output_file:
        output_file.write(decrypted_content)

file_path = r'.txt'

password = ""
salt = ""

decrypt_file(file_path, file_path, password, salt)
print("File encrypted successfully.")

encrypt_file(file_path, file_path, password, salt)
print("File encrypted successfully.")
