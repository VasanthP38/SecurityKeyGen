import random
import time
import turtle as n

seckey = int(input("Generate - \n Pincode(Click '1')         LockPattern(Click '2')"))
if seckey == 1:
    size = int(input("Enter Pincode size: \n"))
    repeat = int(input("Repetition Not Allowed(Click '0')     Repetition Allowed(Click '1')"))
    print("Generating PinCode...")
    time.sleep(1)
    print("Generated")
    time.sleep(0.5)
    l = []
    if repeat == 1:
        for i in range(0, 100):
            a = random.randint(0, 9)
            l.append(a)
    elif repeat == 0:
        for i in range(0, 100):
            a = random.randint(0, 9)
            if a not in l:
                l.append(a)
    fl = l[0:size]
    for i in fl:
        print(i, end=" ")

elif seckey == 2:
    l = []
    tl = []
    for i in range(0, 100):
        a = random.randint(1, 9)
        if a not in tl:
            tl.append(a)
    # print(tl)
    for i in range(0, 9):
        for j in range(0, 8):
            if (tl[j] == 1 and tl[j + 1] == 3) or (tl[j] == 1 and tl[j + 1] == 7) or (tl[j] == 1 and tl[j + 1] == 9) or (tl[j] == 3 and tl[j + 1] == 1) or (tl[j] == 3 and tl[j + 1] == 7) or (tl[j] == 3 and tl[j + 1] == 9) or (tl[j] == 7 and tl[j + 1] == 1) or (tl[j] == 7 and tl[j + 1] == 3) or (tl[j] == 7 and tl[j + 1] == 9) or (tl[j] == 9 and tl[j + 1] == 1) or (tl[j] == 9 and tl[j + 1] == 3) or (tl[j] == 9 and tl[j + 1] == 7):
                tl.append(tl[j + 1])
                tl.pop(j + 1)
            elif (tl[j] == 2 and tl[j + 1] == 8) or (tl[j] == 8 and tl[j + 1] == 2) or (tl[j] == 4 and tl[j + 1] == 6) or (tl[j] == 6 and tl[j + 1] == 4) or (tl[j] == 1 and tl[j + 1] == 7) or (tl[j] == 7 and tl[j + 1] == 1) or (tl[j] == 3 and tl[j + 1] == 9) or (tl[j] == 9 and tl[j + 1] == 3):
                tl.append(tl[j + 1])
                tl.pop(j + 1)
    # print(tl)
    for i in tl:
        if i not in l:
            l.append(i)
    # print(l)

    points = int(input("Enter How Many Dot(s) You Want Us To Connect: (Phone's Default: 4 or Above 4)\n"))
    fl = l[0:points]
    print("Generating LockPattern...")
    print(fl)
    n.color("green")
    n.speed(0)
    n.width(5)
    n.goto(0, 0)
    n.circle(2)
    n.penup()
    n.goto(0, 80)
    n.pendown()
    n.circle(2)
    n.penup()
    n.goto(80, 80)
    n.pendown()
    n.circle(2)
    n.penup()
    n.goto(80, 0)
    n.pendown()
    n.circle(2)
    n.penup()
    n.goto(80, -80)
    n.pendown()
    n.circle(2)
    n.penup()
    n.goto(0, -80)
    n.pendown()
    n.circle(2)
    n.penup()
    n.goto(-80, -80)
    n.pendown()
    n.circle(2)
    n.penup()
    n.goto(-80, 0)
    n.pendown()

    n.circle(2)
    n.penup()
    n.goto(-80, 80)
    n.pendown()
    n.circle(2)
    n.hideturtle()
    n.penup()
    n.speed(2)
    n.color("#00adef")

    for k in fl:
        if k == 1:
            x = -80
            y = 80

        elif k == 2:
            x = 0
            y = 80

        elif k == 3:
            x = 80
            y = 80

        elif k == 4:
            x = -80
            y = 0

        elif k == 5:
            x = 0
            y = 0

        elif k == 6:
            x = 80
            y = 0

        elif k == 7:
            x = -80
            y = -80

        elif k == 8:
            x = 0
            y = -80

        elif k == 9:
            x = 80
            y = -80

        for i in fl:
            if i == fl[0]:
                n.goto(x, y)
                n.pendown()
            else:
                n.goto(x, y)
    print("Generated")
    time.sleep(0.5)
