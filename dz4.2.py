s = "Вне скобок (внутри) вне"
s1 = "("
s2 = ")"
n = ""

s1 = s.find(s1)+1
s2 = s.find(s2)
print(s[s1:s2])