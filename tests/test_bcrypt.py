import bcrypt

password = "123456"

hashed_password = bcrypt.hashpw(
    password.encode(),
    bcrypt.gensalt()
)

print(hashed_password)
print(type(hashed_password))

decoded = hashed_password.decode()

print(decoded)
print(type(decoded))