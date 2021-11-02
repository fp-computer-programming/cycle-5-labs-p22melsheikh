# MEE 11/1/21

string1 = input("What is the first word? ")
string2 = input("What is the second word? ")

if string1 < string2:
    print(string1 + " comes before " + string2)
elif string1 > string2:
    print(string1 + " comes after " + string2)
else:
    print(string1 + " and " + string2 + " are the same")