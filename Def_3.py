name=input()
surname=input()
middlename=input()
def print_initials(name, surname, middlename):
    print(f'{surname.title()} {name[0].title()}.{middlename[0].title()}.')
print_initials(name, surname, middlename)
