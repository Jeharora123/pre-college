def main():
    i=int(input("enter 1 for addition,2 for subtraction,3 for multiplication,4 for division ,5 to EXIT"))
    while i!=5:
        x=int(input("enter num 1: "))
        y=int(input("enter num 2: "))
        if i==1:
            print (x+y)
        elif i==2:
            if x>y:
                print(x-y)
            else:
                 print(y-x)
        elif i==3:
            print(x*y)
        elif i==4:
            print(x/y)
        else:
            print("succesffuly exited")
            break
        i=int(input("new opperation: "))
 
          
main()

