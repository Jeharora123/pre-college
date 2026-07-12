class  Movie:
    def main(self):
        no=int(input("enter number of movies to be checked for:"))
        ratings=[]
        print("enter movies rating:\n")
        for _ in range(no):
            ratings.append(int(input("")))

        obj=Movie()
        obj.calculate_avg(ratings)
        obj.find_highest(ratings)
        obj.countGood(ratings)

    def calculate_avg(self,ratings):
        i=0
        j=0
        for rating in ratings:
            i+=rating
            j+=1
            
        print("average is"+str(i/j))
 
    def find_highest(self,ratings):
        i=ratings[0]
        for rating in ratings:
            if(i<rating):
                i=rating

        print("highest rating is"+str(i))
         
    def countGood(self,ratings):
         i=0
         for rating in ratings:
            if(rating>=8):
                i+=1
                
         print("good movies are:"+str(i))


movie=Movie()
movie.main()
            