
hotel_menu= {
    'main_dish':{
        'Butter Chicken':'RS-150',
        'Paneer Makhani' : 'RS-160',
        'Dal Tadka': 'RS-100',
        'Chicken Biryani':'200'
    },
    'breads':{
        'Naan':'RS-80',
        'Roti' : 'RS-70',
        'Garlic Naan': 'RS-90'
    },
    'rice':{
        'Steamed Basmati Rice':'RS-100',
        'Jeera Rice' : 'RS-120'
    },
    'desserts':{
        'Gulab Jamun':'RS-50',
        'Rasmalai' : 'RS-60',
        'Kulfi': 'RS-70'
    },
    'ice_cream':{
        'Black current':'RS-50',
        'Vanilla' : 'RS-70',
        'Chocolate': 'RS-50',
        'Strawberry':'RS-60'
    },
    'special':{
        'Masala Chai':'RS-20',
        'Mango Lassi' :'RS-50',
        'Fresh Lime Soda': 'RS-30'
    }
}
print(" ############################################################# ")
print("##################### WELCOME ADMIN ############################")
print(" ############################################################# ")
print("[1]PRINT MENU-CARD\n[2]ADD NEW DISH\n[3]UPDATE DISH\n[4]EXIT")
option=int(input("CHOOSE ANYONE OPTION: "))
if option==1:
    for key,value in hotel_menu.items():
        print(f"{key}={value}\n")
elif option==2:
    n=int(input("Enter how many new dish: "))
    for i in range(n):
        menu_name=input("Enter the dish Name you want add in menu card: ").title() 
        n=int(input("how many dish your goint to enter: "))
        new_dish_dic={}
        for i in range(n):
            dish=input("Enter the dish you want to add: ").title() 
            price=int(input(f"Enter price of  {dish} :"))
            new_dish_dic[dish]= price
        #hotel_menu[menu_name]=new_dish_dic
        num=0
        for key,value in new_dish_dic.items():
           num+=1
           print(f"{[num]}{key}={value}")
elif option==3:
    print("\nTHESE ARE THE MENU IN MENU-CARD")
    for i,key in enumerate(hotel_menu):
        previw=key.upper()
        print(f"{[i+1]}{previw}")
    n=0
    update_menu=int(input("plsease selecte the option to update in menu: "))
    if update_menu==1:
        dish=input("Enter the dish you want add in MAIN_DISH: ").title() 
        price=int(input(f"Enter price of  {dish} :"))
        new_dish={dish:price}
        hotel_menu['main_dish'].update(new_dish)
        print("You have successfully added new dish in main dish")
        
        for key,value in hotel_menu['main_dish'].items():
           previw=key.upper()
           n+=1
           print(f"{[n]}{previw}={value}")
    elif update_menu==2:
        dish=input("Enter the dish you want add in BREADS: ").title() 
        price=int(input(f"Enter price of  {dish} :"))
        new_dish={dish:price}
        hotel_menu['breads'].update(new_dish)
        print("You have successfully added new dish in Breads")
        for key,value in hotel_menu['breads'].items():
           previw=key.upper()
           n+=1
           print(f"{[n]}{previw}={value}")
    elif update_menu==3:
        dish=input("Enter the dish you want add in RICE: ").title() 
        price=input(f"Enter price of  {dish} :")
        hotel_menu['rice'][dish]=price
        print("You have successfully added new dish in Rice")
        print("Your updated dish in Rice menu")
        for key,value in hotel_menu['rice'].items():
           previw=key.upper()
           n+=1
           print(f"{[n]}{previw}={value}")
    elif update_menu==4:
        dish=input("Enter the dish you want add in DESSERTS: ").title() 
        price=int(input(f"Enter price of  {dish} :"))
        new_dish={dish:price}
        hotel_menu['desserts'].update(new_dish)
        print("You have successfully added new dish in dessert")
        for key,value in hotel_menu['desserts'].items():
           previw=key.upper()
           n+=1
           print(f"{[n]}{previw}={value}")
    elif update_menu==5:
        dish=input("Enter the dish you want add in ICE_CREAM: ").title() 
        price=int(input(f"Enter price of  {dish} :"))
        new_dish={dish:price}
        hotel_menu['ice_cream'].update(new_dish)
        print("You have successfully added new dish in Ice creame")
        for key,value in hotel_menu['ice_cream'].items():
           previw=key.upper()
           n+=1
           print(f"{[n]}{previw}={value}")
    elif update_menu==6:
        dish=input("Enter the dish you want add in SPECIAL: ").title() 
        price=int(input(f"Enter price of  {dish} :"))
        new_dish={dish:price}
        hotel_menu['special'].update(new_dish)
        print("You have successfully added new dish in special")
        for key,value in hotel_menu['special'].items():
           previw=key.upper()
           n+=1
           print(f"{[n]}{previw}={value}")
    else:
        print("!!!!!!!!!!! SORRY WE DONT HAVE THAT MENU !!!!!!!!")
elif option==4:
    print("!!!!!!!!!BYE!!!!!!!!")  
else:
    print("Invalide input pls check you option")
    
        