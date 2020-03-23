
def process_num(number):
    """
    Processes numbers and if they are divisible by 3 then it returns 'Fizz'
    if they are divisible by 5 returns 'Buzz'
    if they are divisible by 3 and 5 it return 'FizzBuzz'
    other numbers just return themselves

    Keywords args
    number: integer -- number to process
    returns: string or integer
    """

    if number % 3 == 0 and number % 5 == 0:
        return ("FizzBuzz")

    elif number % 5 == 0:
        return ("Buzz")

    elif number % 3 == 0:
        return ("Fizz")

    else:
        return number


if __name__ == '__main__':
    #Processes the numbers 1 - 100 using the process_num function
    for i in range(1, 101):
        print(process_num(i))
