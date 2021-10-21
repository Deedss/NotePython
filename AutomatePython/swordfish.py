while True:
    print('who are you ?')
    name = input()
    if name != 'Joe':
        continue
    print('hello Joe, What is teh password')
    password = input()
    if password == 'swordfish':
        break

print('access granted')
