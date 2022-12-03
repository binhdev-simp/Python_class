num = int(input(" a = "))
if(num//10) <= 99 and (num//10) >= 10:
    tram = num//100
    chuc = (num//10)-tram*10
    case = (tram*100) + (chuc*10)
    donvi = num - case
    if tram == 1:
        st = "mot tram"
    if tram == 2:
        st = "hai tram"
    if tram == 3:
        st = "ba tram"
    if tram == 4:
        st = "bon tram"
    if tram == 5:
        st = "nam tram"
    if tram == 6:
        st = "sau tram"
    if tram == 7:
        st = "bay tram"
    if tram == 8:
        st = "tam tram"
    if tram == 9:
        st = "chin tram"
    
    if chuc == 0:
        sc = "linh"
    if chuc == 1:
        sc = "muoi "
    if chuc == 2:
        sc = "hai muoi"
    if chuc == 3:
        sc = "ba muoi"
    if chuc == 4:
        sc = "bon muoi"
    if chuc == 5:
        sc = "nam muoi"
    if chuc == 6:
        sc = "sau muoi"
    if chuc == 7:
        sc = "bay muoi"
    if chuc == 8:
        sc = "tam muoi"
    if chuc == 9:
        sc = "chin muoi"
    
    if donvi == 0:
        dv = "khong"
    if donvi == 1:
        dv = "mot"
    if donvi == 2:
        dv = "hai"
    if donvi == 3:
        dv = "ba"
    if donvi == 4:
        dv = "bon"
    if donvi == 5:
        dv = "lam"
    if donvi == 6:
        dv = "sau"
    if donvi == 7:
        dv = "bay"
    if donvi == 8:
        dv = "tam"
    if donvi == 9:
        dv = "chin muoi"
        
    if chuc == 0 and donvi == 0:
        sc = ''
        dv = ''
    if donvi == 0:
        dv = ''
    print(st,sc,dv)
else :
    print(num, "khong phai la so co ba chu so")