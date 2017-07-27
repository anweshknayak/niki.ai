


def cipher(m,n):

    arr = [chr(i) for i in xrange(65,90+1)]

    for i in range(m,n+1):
        if(i>26):
            x = i%26
            y = i/26

            if(x==0):
                print arr[y-2] + arr[x-1]
           
            else:
                print arr[y-1] + arr[x-1]

        else:
            print arr[i-1]


#if __name__ == '__main__':
 #   cipher(25,100)