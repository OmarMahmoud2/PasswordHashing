import bcrypt



password = b"thisispassword"

hashed = bcrypt.hashpw(password, bcrypt.gensalt())


print(hashed)

ps = bytes(input('Enter your pass: '), encoding='utf-8')

log = bcrypt.checkpw(ps, hashed)

if log :
    print('logged in successfully')
else:
    print('wrong password, try again')

