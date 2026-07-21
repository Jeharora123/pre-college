class expenseTracker:
    def __init__(self,list,num):
        self.list=list
        self.num=num

    def add_expense(self):
        date=input("enter date in YYYY-MM-DD format: ")
        name=input("enter a name for expense: ")
        ammount=input("enter ammount of expense: ")
        self.list.update({self.num:{name:[date,ammount]}})
        print("succesfully added")
        self.num+=1


    def delete_expense(self):
        name=input("enter the number of expense to be deleted: ")
        for item in self.list:
            if item==name:
                self.list.pop(item)
                print("succesfully removed")

    def view_expenses(self):
        print("ID       NAME        DATE        PRICE")
        for item in self.list:
            b=str(item)
            c=list(self.list[item].keys())[0]

            d=str(self.list[item][c][0])
            e=str(self.list[item][c][1])
            print(b+"       "+c+"       "+d+"       "+e+"       ")

    def summary(self):
        p=0
        for item in self.list:
            p+=int(self.list[item][list(self.list[item].keys())[0]][1])
        print("total expense is: "+str(p))

    def monthsum(self):
        d=input("enter month number in MM form : ")
        p=0
        for item in self.list:
            if self.list[item][list(self.list[item].keys())[0]][0][5:7]==d:
                p+=int(self.list[item][list(self.list[item].keys())[0]][1])
        
        print("total expense for the month is: "+str(p))

def main():
    obj=expenseTracker({},1)
    while True:
        s=int(input("enter 1 to add expense,2 to delete,3 to view,4 for summary,5 for monthly summary,6 for exit"))
        if(s==1):
            obj.add_expense()
        elif(s==2):
            obj.delete_expense()
        elif(s==3):
            obj.view_expenses()
        elif(s==4):
            obj.summary()
        elif(s==5):
            obj.monthsum()
        else:
            break

main()