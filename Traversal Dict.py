word_frq = {"Mayur":20,
            "Sonal":30,
            "Sanvi":40,
            "Shreya":50
            }

#for key in word_frq:
#        print(key)
        
for key,value in word_frq.items():
        if value == 50:
            print(key)
            
print(word_frq.get("Mayur"))

for key in word_frq.values():
    print(key)
    
for key in word_frq.keys():
    print(key)    
    
for key,value in word_frq.items():
    print(key)
    
    
    