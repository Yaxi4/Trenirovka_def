MIN_DRIVING_AGE = 18

def allowed_driving(name, age):
    if age>MIN_DRIVING_AGE:
        print(f'{name} может водить')
    else:
        print(f'{name} еще рано садиться за руль')