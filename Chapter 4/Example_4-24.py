import os

os.listdir('.')

os.listdir(b'.')

pi_name_bytes = os.listdir(b'.')[1]
pi_name_str = pi_name_bytes.decode('ascii', 'surrogateescape')
pi_name_str

pi_name_str.encode('ascii', 'surrogateescape')
