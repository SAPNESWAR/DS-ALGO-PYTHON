def selectionSort(array,size):
    for step in range(size):  #step:0  [20,12,10,15,2]
                              #step:1  [2,12,10,15,20]
        min_idx=step  #min_idx=0

        for i in range (step+1,size): #i=1

            #to sort in descending order,change>to<in this line
            #select the minimum element in each loop
            if array[i]<array[min_idx]:
                min_idx=i  #1 2 4

        # put min at the correct position
        (array[step],array[min_idx])=(array[min_idx],array[step])
data=[20,12,10,15,2]
size=len(data)
selectionSort(data,size)
print('Sorted Array in Ascending Order:')
print(data)
