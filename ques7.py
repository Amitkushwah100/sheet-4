n = int (input("enter a number :"))
for i in range (1,n+1):
     for j in range(n-i):
            print("_" , end =" ")
     for j in range(i):
        print("*" , end =" ")
     print()






# enter a number :5
# _ _ _ _ * 
# _ _ _ * *
# _ _ * * *
# _ * * * *
# * * * * *     