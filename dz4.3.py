s = "бваг агваг ыврря ыврара авяооя"
l = s.split()
for i in range(len(l)):
    if l[i].startswith("а") or l[i].endswith("я"):
        print(l[i])
    i += 1