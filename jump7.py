for a in range(1,101):
    if (a%7)!=0 and (a-7)%10!=0 and (a<70 or a>79):
        print(a)
    else:
        continue
