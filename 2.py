


def cipher(m,n):

    arr = [chr(i) for i in xrange(65,90+1)]

    for i in range(m,n+1):
        if(i>26):
            x = i%26
            print arr[0] + arr[x-1]

        else:
            print arr[i-1]


#if __name__ == '__main__':
#    cipher(25,29)