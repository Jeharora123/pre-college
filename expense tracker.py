def main():
    i=int(input("enter number of expenses needed to be added: "))
    trac={}
    for _ in range(i):
        print("ITEM "+str(_+1)+"\n")
        str1=input("enter expense name for item: " )
        amm=int(input("enter amount for the same: "))
        d=int(input("enter year of entry: "))
        li=[amm,d]
        trac.update({str1:li})
        print("NEXT ENTRY NOW \n")

    for tr in trac:
        print("expense name: "+str(tr)+",  amount is: "+str(trac[tr][0])+", year of entry is:  ",str(trac[tr][1]))
        




main()