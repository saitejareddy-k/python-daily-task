def evenly_divisible (a,b,c):
total = 0
for num in range(a, b + 1):
if num % c == 0:
total
+= num
return total