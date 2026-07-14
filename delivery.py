class Delivery:
    def __init__(self,deliveries):
        self.deliveries=deliveries

    def add_delivery(self,delno,dele):
        self.deliveries.update({delno:dele})

    def remove_delivery(self,delno):
        self.deliveries.pop(delno)

    def display(self):
        for delivery in self.deliveries:
            print(delivery,self.deliveries[delivery])

    def pending_delivery(self):
        for delivery in self.deliveries:
            if(self.deliveries[delivery][1]=="N"):
                print(delivery)

    def complete_delivery(self,delno):
        for delivery in self.deliveries:
            if delivery==delno:
                self.deliveries[delivery][1]="Y"

    def covered_distance(self):
        c=0
        for delivery in self.deliveries:
            if(self.deliveries[delivery][1]=="Y"):
                c+=self.deliveries[delivery][0]

        print("the total amount of ditance covered by the driver is: "+str(c))

    
def main():
    obj=Delivery({})
    obj.add_delivery("001",[5,"N"])
    obj.add_delivery("002",[7,"N"])
    obj.add_delivery("003",[10,"N"])
    obj.add_delivery("004",[2,"N"])
    obj.add_delivery("005",[1,"N"])
    obj.complete_delivery("002")
    obj.covered_distance()
    obj.pending_delivery()
    obj.display()


main()
