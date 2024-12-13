#1
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

#2
s = "Вне скобок (внутри) вне"
s1 = "("
s2 = ")"
n = ""

s1 = s.find(s1)+1
s2 = s.find(s2)
print(s[s1:s2])

#3
s = "бваг агваг ыврря ыврара авяооя"
l = s.split()
for i in range(len(l)):
    if l[i].startswith("а") or l[i].endswith("я"):
        print(l[i])
    i += 1