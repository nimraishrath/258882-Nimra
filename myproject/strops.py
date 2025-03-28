import string
import itertools
def getspan(s,ss):
    span = []
    start = 0
        
    while start < len(s):
        index = s.find(ss, start)  
        if index == -1:
            break
        end = index + len(ss)  
        span.append((index, end))
        start = index + 1 
    return span
def reverseWord(s):
    return ''.join(s.split()[::-1])
def removeallpuntuation(s):
    return ''.join(filter(lambda char : char not in string.punctuation,s))
def countWords(s):
    return len(s.split())
def charmap(s):
    return {char: s.count(char) for char in set(s)}
def maketitle(s):
    return s.title()
def normalizespaces(s):
    return ''.join(s.split())
def transforrm(s):
    return s.swapcase()