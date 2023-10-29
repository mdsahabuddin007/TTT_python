start=datetime.now()
def loop():
    for i in range(1,1000,1):
        yield i

x=loop()
print(next(x))
print(next(x))
##for i in x:
##    print(i)
end=datetime.now()
print("Total Time Takes",(end-start))'''
even=(i for i in range(10) if i%2==0)
print(type(even))
##print(next(even))
##print(next(even))
for i in even:
    print(i)
[10:44 am, 07/10/2023] Dipankar Das: from datetime import datetime
def main(f):
    start=datetime.now()
    f()
    end=datetime.now()
    print("Total Time Takes",(end-start))
@main     
def  even():
    for i in range(1,1000,1):
        if i%2==0:
            print(i)
