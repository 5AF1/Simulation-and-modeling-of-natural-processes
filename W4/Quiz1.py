def question1():
    s0,s1,s2,s3,s4 = [False,False,False,False,False]
    while s4 != True:
        index = int(s0)+2*int(s1)+4*int(s2)+8*int(s3)
        s = int(s0)+int(s1)+int(s2)+int(s3)
        print(f"{index} {s%2}")
        if s0 and s1 and s2 and s3:
            s0, s1, s2, s3 ,s4= [not s0, not s1, not s2, not s3,not s4]
        elif s0 and s1 and s2:
            s0, s1, s2, s3 = [not s0, not s1, not s2, not s3]
        elif s0 and s1:
            s0, s1, s2 = [not s0, not s1, not s2]
        elif s0:
            s0, s1 = [not s0, not s1]
        else:
            s0 = not s0


def question2():
    len = 14
    def value(p2, p1, p0):
        return ((not p2 and p1) or (not p1 and p0) or (p1 and not p0))
    init = len*[False]
    init[10] = True

    for t in range(9):
        tem = len*[False]
        if t != 0:
            for i in range(1,len-1):
                tem[i] = value(init[i-1],init[i],init[i+1])
            init = tem[:]

        print(f"t{t} {init[1:13]}")


question1()
question2()