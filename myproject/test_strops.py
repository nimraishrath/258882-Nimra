import strops
print('-'*80)
s = "mississippi"
ss='iss'
print(f"Span of '{ss}':", strops.getspan(s,ss))

print('*'*80)
print ("str=Hello, world! Python is great.")
print('*'*80)
print(f"Without punctuation:", strops.removeallpuntuation( s="Hello, world! Python is great."))
print('-'*80)
print("Reversed words:", strops.reverseWord( "Hello, world! Python is great."))
print('-'*80)
print("Word count:", strops.countWords( "Hello, world! Python is great."))
print('-'*80)
print('-'*80)
print ("str= banana")
print("Character frequency:", strops.charmap("bannana"))
print('-'*80)
print('-'*80)
print("Title Case:", strops.maketitle("Hello, world! Python is great."))
print('-'*80)
print("Normalization of space:", strops.normalizespaces("Hello, world! Python is great."))
print('-'*80)
print("Trandforme of string:", strops.transforrm("Hello, world! Python is great."))
print('-'*80)



