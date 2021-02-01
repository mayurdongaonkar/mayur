S = '5F3Z-2e-9-w1'
K = 4

def licenseKeyFormatting(plate:str,slice:int):
    plate_clean = plate.replace("-","").lower()
    print("plate clean is  " +  plate_clean)
    
    size = len(plate_clean)
    first_grp  = size%slice
    print("initial pivot is  " + str(first_grp))
    
    ans = str()
    
    if first_grp == 0:
        first_grp = slice
    else:
        first_grp = size%slice
    
    print(ans)
    print(first_grp)
    
    while first_grp < size:
        print(first_grp)
        print(size)
        ans += "-"+ plate_clean[first_grp:slice]
        print(ans)
        first_grp = first_grp + slice
    
    print(ans)
    
    
licenseKeyFormatting(S,K)