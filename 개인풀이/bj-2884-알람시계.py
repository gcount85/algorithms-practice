h, m = map(int, input().split())
if m >= 45:
    mod_m = m - 45
    print(f"{h} {mod_m}")
else:                           # m < 45; 44,43,30,20,0
    mod_m = m + 60 - 45
    if h == 0:
        h = 24
    mod_h = h - 1
    print (f"{mod_h} {mod_m}")