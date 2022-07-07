b = '1234567890'
password=input()
from string import ascii_lowercase

c = ascii_lowercase.upper()
d = '!@#$%*'


def check_password(password):
    count_1 = 0
    count_2 = 0
    count_3 = 0
    if len(password) >= 10:

        for i in password:
            if i in b:
                count_1 += 1
            if i in c:
                count_2 += 1
            if i in d:
                count_3 += 1
    if count_1 > 2 and count_2 > 0 and count_3 > 0:
        print('Perfect password')
    else:
        print('Easy peasy')
check_password(password)