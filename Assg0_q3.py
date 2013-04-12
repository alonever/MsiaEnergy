
def is_palindrome(word):
    i=0
    j=len(word)-1
    while i<=j:
        if word[i] != word[j]:
            return False
        else:
            i = i+1
            j = j-1
        return True
    
print "Testing if RADAR is palindrome: " + str(is_palindrome("radar"))
print "Testing if DIEGO is palindrome: " + str(is_palindrome("diego"))