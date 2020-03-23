def getletter(s, total):
    xs = s.count('x')
    ys = s.count('y')
    zs = s.count('z')
    if xs <= 10 and ys <= 10 and zs <= 10:
        if len(s) == 30:
            # check if s has 10 x's y's and z's
            if xs == 10 and ys == 10 and zs == 10:
                # found a path
                # print(total, s)
                total += 1
        else:
            total = getletter(s + 'x', total)
            total = getletter(s + 'y', total)
            total = getletter(s + 'z', total)

    return total

s = ''
total = 0
print(getletter(s, total))