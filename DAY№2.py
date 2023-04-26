# 1. reverse the array in place (space complexity should be constant)
a = [1,2,3,4,5]
out = []

for i in a:
    out.insert(0,i)

print(out)

# 2. insertan element in between of array

b = [1,2,3,4]
b.insert(3,'value')
# where '3' we would write index