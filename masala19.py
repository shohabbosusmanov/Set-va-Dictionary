words = ['apple', 'banana', 'cherry', 'pineapple', 'grape']
mxln = words[0]
for i in words :
    if len(mxln) < len(i) :
        mxln = i
print(mxln)