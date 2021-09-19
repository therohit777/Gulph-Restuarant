print("--------------------WELCOME TO GULPH RESTUARANT--------------------" )
print("| FOOD MENU |")
print("1. STARTERS: ENTER 1 TO SELECT")
print("2. DRINKS: ENTER 2 TO SELECT")
print("3. DESERTS: ENTER 3 TO SELECT")
sum=0
dict={}
menu="y"
while(menu=="y" or menu=="Y"):
        a=int(input("Sir, what do you wanna have, Please select from above:"))
        if(a==1):
            ask="y"
            while(ask=="y" or ask=="Y"):
                print("--------------------STARTERS MENU--------------------" )
                print("1. MASALA DOSA: Rs.100")
                print("2. CHICKEN WINGS: Rs.150")
                print("3. PEPARONI PIZZA: Rs.349")
                print("4. CHICKEN MOMOS: Rs.100")
                print("5. CHOWMIN: Rs.100")
                print("6. CHICKEN CHOWMIN: Rs.150")
                print("7. BURGER: Rs.125")
                print("8. UTHAPPAM: Rs.250")
                print("9. SANDWICH: Rs.180")
                print("10. CAKE: Rs.185")
                b=int(input("Enter the Serial number of the dish you want to have: "))
                c=int(input("Enter the quantity the dish: "))
                if(b==1):
                    dict["MASALA DOSA"]=c
                    sum+=(c*100)

                elif(b==2):
                    dict["CHICKEN WINGS"]=c
                    sum+=(c*150)
                elif(b==3):
                    dict["PEPARONI PIZZA"]=c
                    sum+=(c*349)
                elif(b==4):
                    dict["CHICKEN MOMOS"]=c
                    sum+=(c*100)
                elif(b==5):
                    dict["CHOWMIN"]=c
                    sum+=(c*100)
                elif(b==6):
                    dict["CHICKEN CHOWMIN"]=c
                    sum+=(c*150)
                elif(b==7):
                    dict["BURGER"]=c
                    sum+=(c*125)
                elif(b==8):
                    dict["UTHAPPAM"]=c
                    sum+=(c*250)
                elif(b==9):
                    dict["SANDWICH"]=c
                    sum+=(c*180)
                elif(b==10):
                    dict["CAKE"]=c
                    sum+=(c*185)
                d=input("Sir,do you want anything else(Y/N):")
                if(d=="y" or d=="Y"):
                    ask=d
                else:
                    break        



        elif(a==2):
            ask="y"
            while(ask=="y" or ask=="Y"):
                print("---------------------DRINKS MENU---------------------" )
                print("1. MANGO SQUASH: Rs.80")
                print("2. ORANGE SQUASH: Rs.80")
                print("3. BLUEBERRY SQUASH: Rs.85")
                print("4. RASBERRI SQUASH: Rs.90")
                print("5. BANANA SHAKE: Rs.100")
                print("6. MILK SHAKE: Rs.100")
                print("7. FRUIT FANTA: Rs.150")
                print("8. HOT CHOCOLATE: Rs.150")
                print("9. STRAWBERRY SHAKE: Rs.180")
                print("10. PINEAPPLE JUICE: Rs.120")
                b=int(input("Enter the Serial number of the dish you want to have: "))
                c=int(input("Enter the quantity the dish: "))
                if(b==1):
                    dict["MANGO SQUASH"]=c
                    sum+=(c*80)
                elif(b==2):
                    dict["ORANGE SQUASH"]=c
                    sum+=(c*80)
                elif(b==3):
                    dict["BLUEBERRY SQUASH"]=c
                    sum+=(c*85)
                elif(b==4):
                    dict["RASBERRI SQUASH"]=c 
                    sum+=(c*90)
                elif(b==5):
                    dict["BANANA SHAKE"]=c
                    sum+=(c*100)
                elif(b==6):
                    dict["MILK SHAKE"]=c
                    sum+=(c*100)
                elif(b==7):
                    dict["FRUIT FANTA"]=c
                    sum+=(c*150)
                elif(b==8):
                    dict["HOT CHOCOLATE"]=c
                    sum+=(c*150)
                elif(b==9):
                    dict["STRAWBERRY SHAKE"]=c
                    sum+=(c*180)
                elif(b==10):
                    dict["PINEAPPLE JUICE"]=c
                    sum+=(c*120)
                d=input("Sir,do you want anything else(Y/N):")
                if(d=="y" or d=="Y"):
                    ask=d
                else:
                    break  

        elif(a==3):
            while(ask=="y" or ask=="Y"):
                print("---------------------DESERTS MENU---------------------" )
                print("1. OREO CORNATO: Rs.60")
                print("2. PADALPOPS: Rs.50")
                print("3. ROSOGULA: Rs.35")
                print("4. ICECREAM: Rs.50")
                print("5. CHOCOLATES: Rs.80")
                print("6. VANILLA ICEREAM: Rs.70")
                print("7. KALAKAND: Rs.50")
                print("8. BLACK FOREST: Rs.140")
                print("9. POPBURST: Rs.150")
                print("10. FROZEN CHOCOLATE: Rs.120")
                b=int(input("Enter the Serial number of the dish you want to have: "))
                c=int(input("Enter the quantity the dish: "))
                if(b==1):
                    dict["OREO CORNATO"]=c
                    sum+=(c*60)
                elif(b==2):
                    dict["PADALPOPS"]=c
                    sum+=(c*50)
                elif(b==3):
                    dict["ROSOGULLA"]=c
                    sum+=(c*35)
                elif(b==4):
                    dict["ICECREAM"]=c
                    sum+=(c*50)
                elif(b==5):
                    dict["CHOCOLATE"]=c
                    sum+=(c*80)
                elif(b==6):
                    dict["VANILLA ICECREAM"]=c
                    sum+=(c*70)
                elif(b==7):
                    dict["KALAKAND"]=c
                    sum+=(c*50)
                elif(b==8):
                    dict["BLACK FOREST"]=c
                    sum+=(c*140)
                elif(b==9):
                    dict["POPBURST"]=c
                    sum+=(c*150)
                elif(b==10):
                    dict["FROZEN CHOCOLATE"]=c
                    sum+=(c*120)
                d=input("Sir,do you want anything else(Y/N):")
                if(d=="y" or d=="Y"):
                    ask=d
                else:
                    break  
    
        
        f=input("Sir,do you want anything else from other menus(Y/N):")
        if(f=="y" or f=="Y"):
            menu=f
        else:
            break 
print("--------------------------TOTAL BILL--------------------------")
print("TOTAL AMOUNT: Rs.",sum)
print("GST: 10%")
print("ITEMS  :  QUANTITY")
for i in dict:
    print(i+":",dict[i])
gst=sum*0.1
total=sum+gst
print("TOTAL BILLING AMOUNT: Rs.",total)