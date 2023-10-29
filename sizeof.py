##for i in range(100):
##    if i%2==0:
##        print(i)
import sys
##d=[i for i in range(100) if i%2==0]
##print(d)
d=[i for i in range(1000)]
print(sum(d))
print(sys.getsizeof(d))
print(type(d))
d2=(i for i in range(1000))
print(sum(d2))
print(sys.getsizeof(d2))
print(type(d2))
