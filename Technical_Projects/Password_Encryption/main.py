import bcrypt

#must be byte string
password = b"SecretPassword55"
hashed = bcrypt.hashpw(password, bcrypt.gensalt())

if bcrypt.checkpw(password, hashed):
    print("It matches")
else:
    print("Didn't Match")