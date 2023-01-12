def add_binary(a, b):

    while True:
        try:
           a = int(input('1st Binary: '), 2)
        except ValueError:
            print('not valid try again')
            continue
        try:
            b = int(input('2nd Binary: '), 2)
        except ValueError:
            print('not valid try again')
            continue
        else:
            result = (bin(a + b)[2:])
            print(result)
        break
    return result


add_binary(1,1)
