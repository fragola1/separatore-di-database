import sys

db = sys.argv[1]
output = 'output'


def save(filename, content):
    file = open(f'{output}/{filename}.txt', 'a')
    file.write(f'{content}\n')
    file.close()


for login in open(db, encoding='utf8'):
    try:
        login = login.strip()
        email = login.split('@')[1].split(':')[0]
        save(email, login)
    except Exception as e:
        print(f'{login} -> {e}')
