def get_first_element(lst):
    print(lst[0])  


n = int(input("Enter the number of elements in the list: ")) 
user_list = []  

for _ in range(n):
    element = input("Enter an element: ")  
    user_list.append(element) 

# Call the function
get_first_element(user_list)
