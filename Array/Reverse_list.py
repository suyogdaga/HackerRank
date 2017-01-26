
def reverse_in_place(lst):      # Declare a function
    size = len(lst)             # Get the length of the sequence
    hiindex = size - 1
    its = size/2                # Number of iterations required
    for i in xrange(0, its):    # i is the low index pointer
        temp = lst[hiindex]     # Perform a classic swap
        lst[hiindex] = lst[i] 
        lst[i] = temp
        hiindex -= 1            # Decrement the high index pointer
    print "Done!"

# Now test it!!
array = [2, 5, 8, 9, 12, 19, 25, 27, 32, 60, 65, 1, 7, 24, 124, 654]

print array                    # Print the original sequence
reverse_in_place(array)        # Call the function passing the list 
print array                    # Print reversed list