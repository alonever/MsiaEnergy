
def bubbleSortAsc(listing):
    listing = list(listing)
    for i in range(len(listing)):
        for j in range(i+1, len(listing)):
            if listing[i] > listing[j]:
                listing[i], listing[j] = listing[j], listing[i]
    return listing
                
def bubbleSortDsc(listing):
    listing = list(listing)
    for i in range(len(listing)):
        for j in range(i+1, len(listing)):
            if listing[i] < listing[j]:
                listing[i], listing[j] = listing[j], listing[i]
    return listing

numbers = [19,20,50,21,54,98,12,4,75,2,14,9,88,20] # change here for the testing numbers

print "Please choose the order you want to sort (1 for Ascending, 2 for Descending)"
order = raw_input("> ")
if "1" in order:
    print "The ascending order of the numbers are:"
    print bubbleSortAsc(numbers)
elif "2" in order:
    print "The descending order of the numbers are:"
    print bubbleSortDsc(numbers)
else:
    print "I don't understand it."