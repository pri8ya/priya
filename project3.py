test_list=[1,4,6,7,8]
print("original list is: "  + str(test_list))

print("list index-value are : ")
for index, value in enumerate(test_list):
     print(index, value)

#tuple

mylist=("c","c++")

print(mylist[0])

#deleting different dictionary elements

thisdict={
    "brand"  : "ford",

    "model" : "mustang",

    "year" : "1964"

    }
del thisdict["model"]
print(thisdict)
