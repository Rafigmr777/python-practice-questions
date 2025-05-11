#lst = list(input("Please enter the list of integers").split())
lst = list(map(int, input("Enter list of integer elements").split()))
print(len(lst))
print(type(lst))
found = False
k = int(input("Please enter the sum number"))
for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if (lst[i] + lst[j]) == k:
            #lst[j]+=1
            print(f'we found the sum {k} which equals {lst[i]} and {lst[j]}')
            found = True
    if found:
        break
if found == False:
    print("We could not find the sum which eqauls",k)
            
            #lst[i]+=1
        
        
    
        
        
        
    
       

