#Match Statement
weeks = 'Tuesday'
match weeks:
    case 'Monday':
        print('Welcome to Monday')
    case 'Tuesday':
        print('2nd day of the week')
    case 'Wednesday':
        print('3rd day of the week')
    case _:
        print('Waiting for this day')