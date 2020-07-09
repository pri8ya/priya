#program to display the fibonacci sequence up to n-th term

nterms=int(input("how many terms?"))

#first two terms
n1, n2 = 0, 1
count = 0

#check if the number of terms is valid
if nterms <=0:
    print("please enter a positive integer")
elif nterms == 1:
    print("fibonacci sequence upto",nterms,":")
    print(n1)
else:
    print("fibonacci sequence:")
    while count < nterms:
        print(n1)
        nth=n1  + n2
        #update values
        n1=n2
        n2=nth
        count += 1
        
