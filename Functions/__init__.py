def line():
    print('-' * 50)

def title(msg):
    line()
    print(msg.center(50))
    line()


def verify():
    from random import randint
    machine = randint(0, 10)
    number_user = int(input('Kick a number between 0 - 10: '))
    line()
    while True:
        if number_user < machine:
            number_user = int(input('You kicked wrong. The number machine is higher!\n'
                                    'Try again: '))
            line()
        elif number_user > machine:
            number_user = int(input('You kicked wrong. The number machine is less!\n'
                                    'Try again:  '))
            line()
        elif number_user == machine:
            print(f'Correct, the number of the machine was {machine}.')
            line()
            break
