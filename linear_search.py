 
 
list_1 = []
Choice  = 'Y'
while (Choice == 'Y'):
    print ("WELCOME TO LINEAR SEARCH")
    n = int(input("Enter the size of list:"))
    for i in  range ( 0 , n ):
        element_in_list = int(input(f'Enter the element{i} in the list:'))
        list_1.append(element_in_list)
    print(list_1)
    searching_element = int(input("Enter the searching element :"))
    for i in range ( 0 , n):
        if (searching_element == list_1[i]):
            print(" The element is found at index ", i)
            break 
    else :
        print("The element is not found!!! ")
    Choice = input(" You want to continue this code ('Y' for yes and 'N' for no)")
    if (Choice=='N'):
        print("Thankyou for doing this code !!!!!")