s = "abcdefghi"

print(s[: :])
print(s[3:6])
print(s[3:6:2])
print(s[: : -1])
print(s[4:1:-2])


for index in range(len(s)):
    if s[index] == 'i' or s[index] == 'u':
        print("There is an i or")

    
for char in s:
    if char == 'i' or char == 'u':
        print("There is an i or u")


s2 = "6.00 is 6.0001 and 6.0002"
new_str = ""
new_str += s2[-1]
print(new_str)
new_str += s2[0]
print(new_str)
new_str += s2[4::30]
print(new_str)
new_str += s2[13:10:-1]
print(new_str)