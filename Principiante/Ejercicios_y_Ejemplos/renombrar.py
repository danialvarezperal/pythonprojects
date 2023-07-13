#!/usr/bin/python3

import os

def main(): 
    for count, filename in enumerate(os.listdir(routeFile)):

        if filename.endswith(".png"):
            dst ="Captura_" + str(count) + ".png"
            src = routeFile + "/" + filename 
            dst = routeFile + "/" + dst 
            
            print(dst)
            
            os.rename(src, dst)
        elif filename.endswith(".jpg"):
            dst ="Captura_" + str(count) + ".jpg"
            src = routeFile + "/" + filename 
            dst = routeFile + "/" + dst 
            
            print(dst)
            
            os.rename(src, dst)
            
        else:
            print("Fichero no PNG salto al siguiente ")

isDirectory = int(input("Si estas en la ruta del archivo pulsa 1, si no pulsa 2: "))
if isDirectory == 1:
    routeFile = os.getcwd()
else :  
    routeFile = input("Ruta del archivo: ")

if __name__ == '__main__': 

      
    main() 
