class Room:
    def __init__(self,rooms):
        self.rooms=rooms

    def book_room(self,type):
        i=0
        c=0
        for room in self.rooms[type]:
            if room=="A":
                self.rooms[type][c]="B"
                i+=1
                break
            c+=1
        if(i==0):
            print("ROOM NOT AVAILABLE")


    def cancel_booking(self,type):
        i=0
        for room in self.rooms[type]:
            if room=="B":
                self.rooms[type][i]="A"
                break
            i+=1

    def calculate_bill(self,nights,type):
        bill=0
        if type=="suite":
            bill+=10000*nights
        else:
            bill+=5000*nights

        if(nights>=7):
            bill=bill*90/100
        
        print("TOTAL BILL AFTER DISCOUNT IS:",str(bill))

    def add_room(self,type):
        self.rooms[type].append("A")

    def main():
        rooms={"single":[],"suite":[]}
        obj=Room(rooms)
        obj.add_room("suite")
        obj.add_room("suite")
        obj.add_room("suite")
        obj.add_room("single")
        obj.add_room("single")
        obj.add_room("single")
        obj.add_room("single")
        obj.add_room("single")
        obj.book_room("suite")
        obj.book_room("suite")
        obj.book_room("suite")
        obj.book_room("suite")
        obj.calculate_bill(10,"suite")

Room.main()
        
