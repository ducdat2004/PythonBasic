while 1:
    try:
        s = input().strip().lower()
        bangChuCai = [0] * 26
        for i in s:
            if i.isalpha():
                bangChuCai[ord(i) - ord('a')] = 1 # Neu trong chuoi xuat hien mot ki tu trong bang chu cai tu a den z thi gan = 1, Va sau do kiem tra neu trong list bangchucai co gia tri 0 co nghia la co 1 chu khong xuat hien
        c = lambda bangChuCai: "YES" if len([i for i in bangChuCai if i == 1]) == 26 else "NO"  
        print(c(bangChuCai))
    except:
        break