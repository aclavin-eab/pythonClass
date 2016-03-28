#Author: Andrew Clavin

#6.2.2 (page 259)
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
#6.3.17 and 18 (page 269-270). These two functions are the same problem: one checks the other.  Make sure your functions produce the correct results
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


