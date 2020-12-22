# set up option to repeat calculation
option = 'y'
while (option == 'y'):

    # get position
    check = 1
    while (check == 1):
        print("enter initial position: ")
        x0 = input()
        try:
            x0 = float(x0)
            check = 0
        except:
            check = 1
            print("value entered is not a number. enter a number: ")

    # get velocity
    check = 1
    while (check == 1):
        print("enter initial velocity: ")
        v0 = input()
        try:
            v0 = float(v0)
            check = 0
        except:
            check = 1
            print("value entered is not a number. enter a number: ")
            

    # get acceleration
    check = 1
    while (check == 1):
        print("enter acceleration: ")
        a = input()
        try:
            a = float(a)
            check = 0
        except:
            check = 1
            print("value entered is not a number. enter a number: ")

    # get time
    check = 1
    while (check == 1):
        print("enter time: ")
        t = input()
        try:
            t = float(t)
            check = 0
        except:
            check = 1
            print("value entered is not a number. enter a number: ")

    #ensure time entered is not negative
    while (t < 0):
        print("time entered is negative. enter a time of at least 0: ")
        t = input()
        t = float(t)

    # calculate xF, final velocity
    xf = x0 + v0 * t + 0.5 * a * t * t

    # print result sequentially
    print("x0 =", x0)
    print("v0 =", v0)
    print("a =", a)
    print("t =", t)
    print("\n")
    print("xf = ", x0, "+", v0, "*", t, "+ 0.5 *", a, "*", t, "*", t)
    print("xf = ", x0, "+", v0, "*", t, "+ 0.5 *", a, "*", t * t)
    print("xf = ", x0, "+", v0 * t, "+", 0.5 * a * t * t)
    print("xf = ", xf)
    print("\nEnter 'y' to perform another calculation: ")
    option = input()

    
