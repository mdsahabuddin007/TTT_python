try:
    x=open("D:\Anudip\Data.txt",'a')
    print(x)
    x.write("Anudip Python Content")
    x.write(str(25))
    x.write("\n")
    x.write("ABC KOLKATA")
    print("File Created Successfully")
    x.close()
except FileNotFoundError:
    print("File not Present")
 try:
    with open("D:\\Anudip\\Data.txt","r") as x:
        print(x.read())
    print(x.closed)
except FileNotFoundError:
    print("File not Present")
##import pickle
##x=[i for i in range(1,200,1)]
##with open("data.pkl","wb") as file:
##    pickle.dump(x,file)
import pickle
with open("D:\\data.pkl","rb") as  file:
    x=pickle.load(file)

print(x)
