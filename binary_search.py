list_1 = []
n = int(input("Enter the size of list :"))
for i in range(0,n):
    inserting_element = int(input(f"Enter the {i} element in list :" ))
    list_1.append(inserting_element)
print(list_1)

for i in range(0, n):
    print("lis[", i, "] = ", i )

s_element= int(input("Enter the searching element :"))

first = 0 
last = n-1

while(first<=last):
    middle = int((first + last)/2)
    if (s_element==list_1[middle]):
        print("Element is found at index :",middle)
        break
    elif(s_element > list_1[middle]):
        first = middle+1
    else:
        last = middle-1

if(first > last):
    print("Element not found")
