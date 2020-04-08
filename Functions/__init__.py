# Create a line.
def line():
    print('-' * 50)

# Centralizes the title.
def title(msg):
    line()
    print(msg.center(50))
    line()

# Checks the value entered by the user.
def verify():
    from random import randint
    machine = randint(0, 10)
    try:
        number_user = int(input('Kick a number between 0 - 10: '))
    except:
        print('That is not a number, try again.')
        line()
        return verify()
    else:
        line()
        while True:
            if number_user < machine:
                print('You kicked wrong. The number machine is higher!\n'
                      'Try again: ')
                line()
                return verify()
                line()
            elif number_user > machine:
                print('You kicked wrong. The number machine is less!\n'
                      'Try again:  ')
                line()
                return verify()
                line()
            elif number_user == machine:
                print(f'Correct, the number of the machine was {machine}.')
                line()
                break
