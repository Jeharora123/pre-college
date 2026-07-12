class  Scoreboard:
    def __init__(self,runs,wickets,balls):
        self.runs=runs
        self.wickets=wickets
        self.balls=balls
            
    def add(self,runs):
        self.runs+=runs
        return(self.runs)

    def wicket(self):
        self.wickets+=1
        if(self.wickets>2):
            return("match over")
        else :
            return("")

    def display(self):
        print(str(self.runs)+"/"+str(self.wickets))
        print(self.balls)

    def main(self):
        obj=Scoreboard(0,0,0)
        c=0
        print("WELCOME TO 10 BALL GAME")
        s=int(input("enter target to be chased: "))
        print("enter 10 balls results-1,2,3,4,5,6,0 or W")
        for _ in range(10):
            l=obj.add(0)
            if(l>s):
                break

            t=input("ball "+str(_+1)+": ")
            if t=="W":
               st= obj.wicket()
               if (st=="match over"):
                   c+=1
                   break
                   
            else :
                obj.add(int(t))

        i=obj.add(0)
        if(c==0 and i>s):
            print("u won")
        else:
            print("u lose")
 
sc=Scoreboard(0,0,0)
sc.main()

            
