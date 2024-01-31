s=input("Enter a word: ")
res= " "
for char in s:
    if char.lower() not in "aeiou":
        res +="_"
    else:
        res+=char
print(res)
