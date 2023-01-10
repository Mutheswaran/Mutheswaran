def maxArea(A, Len) :
    area = 0
    for i in range(Len) :
        for j in range(i + 1, Len) :
           
            area = max(area, min(A[j], A[i]) * (j - i))
    return area
 
a = [ 1, 5, 4, 3 ]
b = [ 3, 1, 2, 4, 5 ]
 
len1 = len(a)
print(maxArea(a, len1))
 
len2 = len(b)
print(maxArea(b, len2))
 
