def delchar(s,c):
    if len(c)==1:
        for i in s:
            if c!=i:
                print(i,end="")
    else:
        print(s)
delchar('good evening','o')
