sentence = input('Enter your sentence: ')
l=len(sentence)
cons=0
vow=0
for i in  sentence:
    if i not in 'aeiouAEIOU':
        cons=cons+1
        continue
    print(i)
vow=l-cons
print("number of vowels in the given string is",+vow)
    
        
