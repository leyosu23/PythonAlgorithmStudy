def gcd(a,b):
    if(a%b == 0):
        return b
    else:
        print(a, a%b)
        return gcd(a, a % b)


print('result: ' + str(gcd(182, 64)))