
"""
The nth term of the sequence of triangle numbers is given by, t_n = (1/2)*n*(n+1); so the first ten 
triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position 
and adding these values we form a word value. For example, the word value for SKY 
is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the 
word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly 
two-thousand common English words, how many are triangle words?
"""

#All the words in the file have score less than 100*101/2
triangles = set()
for i in range(1,100):
    triangles.add(i*(i+1)/2)

def word_to_num(word):
    total = 0
    for c in word:
        #All words are uppercase
        total += ord(c) - ord('A') + 1
    return total
        

#extract words from file
words = open('words.txt').read().replace('"', '').split(',')

total = 0
for word in words:
    #print word,word_to_num(word)
    if word_to_num(word) in triangles:
        total += 1

print total


