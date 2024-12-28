# Z pattern program ....

A="";    
for i in range(0,7):    
    for j in range(0,7):     
        if (((i == 0 or i == 6) and j >= 0 and j <= 6) or i+j==6):  
            A=A+"#"    
        else:      
            A=A+" "    
    A=A+"\n"    
print(A) 
