##The first step is to create our array with our list and target
arr1 = [3, 1, 5, 6]
target1 = 8

##This second array is a 'false' one - it should return nothing as there's no two sums!
##Having the two arrays allows us to compare the results but you could just have one
arr2 = [4, 7, 2, 6]
target2 = 12

##Next we create a function (a block of code which only runs when it is called)
##We have two arguments: arr and target
##We take the array and target value
##Returns two positions that sum up to the value e.g. [0, 1]
##We use a dictionary to map the number to the position in the array e.g 3 = position 0 
##We can use a for loop
##Enumerate lets us count the loop and value the item at the iteration: Checking the position and elements
##Each element we're going to work out the compliment of the value
##When we've computed the compliment - we're going to check if it's a key in the dict
##If it is, yay we've found two elements that work
##We can return a list with the values of the compliment index and the current index
##If the compliment is not in the array, we can move onto the next element
##If none of the indices match, there's no two indices that sum up to the target value
##So, we can return an empty list

def two_sum(arr, target):
    values = dict() 

    for i, elem in enumerate(arr):
        compl = target - elem

        if compl in values:

            return [values[compl], i]

        values[elem] = i

    return []

##Here we can run our two imputs

list1 = two_sum(arr1, target1,)
print(list1)

list2 = two_sum(arr2, target2)
print(list2)
