'''
You have two arrays A and B.
The two arrays are composed of N elements, and both elements are natural numbers.
You can perform up to K times of replacement operation.
Replacement operation is a swapping two elements by selecting one element from array A and array B.
Print the maximum value of the sum of all elements of Array A.
'''

n,k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break
print(sum(a))
