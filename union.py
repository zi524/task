def get_array(array):
    a=int(input("Enter array length?\n"))
    for i in range(a):
        array.append(int(input("array elements follow by enter")))
    return array        
def remove_duplicates_using_set(arr):
    seen = set()
    unique_elements = []
    for elem in arr:
        if elem not in seen:
            seen.add(elem)
            unique_elements.append(elem)
    return unique_elements
def get_union(arr1,arr2):
    return arr1+arr2    
def get_intersect(arr1,arr2):
    return list(set(arr1).intersection(arr2))
if __name__ == "__main__":
    array1=[]
    array2=[]
    union=[]
    intersection=[]
    array1=get_array(array1).copy()
    array2=get_array(array2).copy()
    array1=remove_duplicates_using_set(array1).copy()
    array2=remove_duplicates_using_set(array2).copy()
    union=get_union(array1,array2)
    intersection=get_intersect(array1,array2)
    print("union =",union)
    print("intersection=",intersection)