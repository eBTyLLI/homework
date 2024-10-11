s = "Н !нннн н!нн ннн! !!! н ннн!ннн!"
L = 0
l = 0

for i in range(len(s)):
    if s[i] == "н":
        l += 1
if l > L:
    L = l
else:
    l = 0
for i in range(len(s)):
    if s[i] == "!":
        s = s.replace("!", ".")

print("Самая длинная последовательность букв 'н':", L)
print("Строка:", s)