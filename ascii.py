def ascii_capitalize
result
(input_str):
= ""
for char in input_str:
if 
ord (char) % 2 == 0:
result
+= char.upper()
else :
result += char .Lower()
return result