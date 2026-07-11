class Jar:
    def __init__(self, capacity=12):
      self._capacity=capacity   
      self._size=0

    def __str__(self):
        i=self.size
        print(i*"🍪")
   
    def deposit(self, n):
        if(self.size+n>self.capacity):
            print("error too much")
        else:
           self._size+=n

    def withdraw(self, n):
        i=self.size
        if(i-n<0):
            print("error too less")
        else:
           self._size-=n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
        
j=Jar()
j.deposit(5)
j.withdraw(4)
j.deposit(11)
print(j)
