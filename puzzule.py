"""
First
061512121523 152118 0914192007180113 16010705
Second
19051404 13051919010705 09 0113 01 2018050119211805 082114200518
And
23010920 152118 1805161225

"""
ss = ""

for i in "061512121523 152118 0914192007180113 16010705":
    if i == ' ':
        ss += i
    else:
        ss += chr(97 + int(i))

print(ss)
print(ss.replace('b', ' '))
"""
The binary conversion of the number 061512121523152118091419200718011316010705 is

The string conversion of the binary number is

"3\u0018\u001a\u001a\u0012\u0014\u0014\u0018\u0019\u000a\u000e\u0013\u0013\u0010\u0000\u0007".

convert this to alphabet characters 3\u0018\u001a\u001a\u0012\u0014\u0014\u0018\u0019\u000a\u000e\u0013\u0013\u0010\u0000\u0007
The alphabet characters for the string 3\u0018\u001a\u001a\u0012\u0014\u0014\u0018\u0019\u000a\u000e\u0013\u0013\u0010\u0000\u0007 are
 "CJETKJIIS".


"""
