class Movie:
    def __init__(self,seats,price):
        self.price=price
        self.seats=seats

    def view(self):
        for seat in self.seats:
            if self.seats[seat]=="A":
                print(seat)

    def book(self):
    
        i=int(input("enter number of tickets to be booked"))
        for _ in range(i):
            j=int(input("seats 1-5 cost 500,the rest cost 200 \n enter seat number: "))
            if self.seats[j] !="B":
             self.seats[j]="B"
            else:
             print("book another seat,this one is taken")
            if(j<=5):
                self.price+=500
            else:
                self.price+=200

            
        

    def cancel(self):
         
        i=int(input("enter number of tickets to be cancelled"))
        for _ in range(i):
            j=int(input("enter seat number to be cancelled,u will get 300 back for a 500rp wicket and 100 for a 200 rp "))
            if(j<=5):
                self.price-=500
            else:
                self.price-=200

            self.seats[j]="A"

    def bill(self):
        print("TICKETS BOOKED:")
        for seat in self.seats:
            if(self.seats[seat]=="B"):
                print(seat)

        print("total bill for ur movie is: "+str(self.price))
             
        

def main():
    seats={}
    for _ in range(20):
        seats.update({_+1:"A"})
    obj=Movie(seats,0)
    obj.view()
    obj.book()
    obj.cancel()
    obj.bill()    

main()