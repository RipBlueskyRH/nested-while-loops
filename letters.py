#Write a program to check how many times a character is repeated in a word?
word = str (input("enter a word"))
letter= str (input("enter a letter"))
i=0
count=0
while i<len(word):
    if word[i]==letter:
        count+=1
    i+=1
print(count)