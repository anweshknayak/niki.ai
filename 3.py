import sys
import math

def func(num):

        if(num>100000):
            sys.exit()

        factors = [x for x in range(2,num+1) if num%x==0]
        print factors

        prime = all([num % x for x in range(2,int(num**0.5)+1)])
        if(prime):
            print "prime"
        else:
            print "not prime"

#if __name__ == '__main__':
#        func(100)