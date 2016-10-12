
def round(x):
    i = 0
    a = 0
    while x>a:
        i += 1
        a += 6 * i
    print i, a

round(37)