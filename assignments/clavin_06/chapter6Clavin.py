#Author: Andrew Clavin

#6.2.2 (page 259)
'''Write a function that reads a text file from the web
at the given URL and returns the number of words in the file
using the final wordCount5 function from Section 6.1.
You can test your function on books from
Project Gutenberg at http://www.gutenberg.org.
For any book, choose the “Plain Text UTF-8” or ASCII version.
In either case, the file should end with a .txt file extension.
For example, should return the number of words in A Tale of Two Cities by
Charles Dickens. You can also access a mirrored copy of A Tale of Two Cities
from the book web site at
http://discovercs.denison.edu/chapter6/ataleoftwocities.txt'''
import urllib.request as web

def wordCount5(text):
    count = 0
    prevCharacter = ' '
    for character in text:
        if character in ' \t\n' and prevCharacter not in ' \t\n':
            count = count + 1
        prevCharacter = character
    if prevCharacter not in ' \t\n':
        count = count + 1
    return count

def wcWeb(url):
    webpage = web.urlopen(url)
    text = webpage.read()
    wordCount = wordCount5(text.decode('utf-8'))
    return wordCount    

print(wcWeb('http://www.gutenberg.org/cache/epub/98/pg98.txt'))

#6.3.17 and 18 (page 269-270). These two functions are the same problem:
#one checks the other.
#Make sure your functions produce the correct results
'''6.3.17. Similar to parity in Exercise 6.1.11,
a checksum can be added to more general strings to detect errors
in their transmission.
The simplest way to compute a checksum for a string is to
convert each character to an integer representing its position in the alphabet
(a = 0, b = 1, …, z = 25), add all of these integers,
and then convert the sum back to a character.
For simplicity, assume that the string contains only lower case letters.
Because the sum will likely be greater than 25,
we will need to convert the sum to a number between 0 and 25
by finding the remainder modulo 26.
For example, to find the checksum character for the string ‘snow’,
we compute (18 + 13 + 14 + 22) mod 26
(because s = 18, n = 13, o = 14 and w = 22),
which equals 67 mod 26 = 15. Since 15 = p,
we add ‘p’ onto the end of ‘snow’ when
we transmit this sequence of characters.
The last character is then checked on the receiving end.
Write a function that returns word
with the appropriate checksum character added to the end.
For example, checksum(‘snow’) should return ‘snowp’.
(Hint: use chr and ord.)
6.3.18. Write a function that determines whether the checksum character
at the end of word (see Exercise 6.3.17) is correct.
For example, checksumCheck(‘snowp’) should return True,
but checksumCheck(‘snowy’) should return False.'''
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def checksum(word):
    total = 0;
    for letter in word:
        for i in range(len(alphabet)):
            if letter == alphabet[i]:
                total += i
    print(total)
    word = word + alphabet[total % 26]
    print(word)
    return word

print(checksum("hello"))

def checksumCheck(word):
    check = False
    cs = word[-1]
    word = word[:-1]
    total = 0
    for letter in word:
        for i in range(len(alphabet)):
            if letter == alphabet[i]:
                total += i
    print(total)
    return alphabet[total % 26] == cs

test = checksum("hello")
print(checksumCheck(test))

#6.6.4 (page 296)
'''6.6.4. Repeat Exercise 6.6.3, but make it work correctly
even if the two strings have different lengths.
In this case, each “missing” bit at the end of the shorter string
counts as one toward the Hamming distance.
For example, hamming(’000’, ‘10011’) should return 3.'''
def hamming(bits1, bits2):
    distance = abs(len(bits1) - len(bits2))
    if len(bits1) >= len(bits2):
        for bit in range(len(bits2)):
            if bits1[bit] != bits2[bit]:
                distance += 1
    else:
        for bit in range(len(bits1)):
            if bits1[bit] != bits2[bit]:
                distance += 1
    return distance
print(hamming('000', '10011'))


