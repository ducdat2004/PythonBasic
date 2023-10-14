
s = input().strip().replace(" ", "")
ns = ""
for i in s:
    if not(i.isalnum()):
        ns += ' '
    else:
        ns += i
ten, cu, moi = ns.split()
print(abs((int(moi) - int(cu) * 1200)))