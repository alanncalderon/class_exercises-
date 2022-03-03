text="a nut for a jar of tune"
text=text.replace(" ","")
print(text)
reversed= text[::-1]
if text==reversed:
    print("this is a palindrome")
else:
    print("This is not a palindrome")