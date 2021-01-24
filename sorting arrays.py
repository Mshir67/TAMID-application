
arr1 = [1,2,3,4,5,7,8,9,10]                     # Test Sorted array #1
arr2 = [4,5,6,7,8,9]                            # Test Sorted array #2

num = input("Enter value: ");                   # value k


def sortArrays(a1,a2, k):
    print(sorted(a1+a2)[:int(k)])               # combines two arrays then sorts them and prints the first k values
    

print("Array 1: " + str(arr1))
print("Array 2: " + str(arr2))
print("Number (k): " + num)

sortArrays(arr1,arr2,num);                      # calls the functions and passes variables
    
    

    

