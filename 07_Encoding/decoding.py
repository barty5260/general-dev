import base64

file_path = r'.txt'

file_encode = base64.b64decode(open(file_path, 'rb').read())

with open(file_path, 'wb') as output:
    output.write(file_encode)