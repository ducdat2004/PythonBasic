s = input().lower().split()
email = ""
for i in s:
    if i != s[-1]:
        email += i[0]
email += (s[-1] + "@huscmail.edu.vn").strip()
print(email)