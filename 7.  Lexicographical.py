def lexo(my_string):
    words = my_string.split()
    words.sort()
    for i in words:
        print( i )
if __name__=='__main__':
    my_string = " i am very tired"\
    " need to take rest"
lexo(my_string)
