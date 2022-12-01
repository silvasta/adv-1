#------------------------------------------------------------------------------------
#Listen teilen

rein = open("Koordinatenliste.dat", "r")                                    
inhalt = rein.readlines()                       
rein.close()                                     
X=[]; Y=[]                   
for i in inhalt:                              
                    
    x,y = i.split()  
    X.append(float(x))                   
    Y.append(float(y))

print("X: ", (X))             
print("Y: ", (Y))