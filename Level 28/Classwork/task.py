

# upper() - ყველა ასოს გარდაქმნის დიდ ასოდ


# lower() - ყველა ასოს გარდაქმნის პატარა ასოდ


# capitalize() - მხოლოდ პირველი ასო გადააქცევს დიდად, ხოლო დანარჩენებს პატარა ასოდ


# find() - ეძებს კონკრეტულ სიმბოლოს ან სიტყვას და აბრუნებს მის ინდექსს (პირველივე პოვნისას); თუ ვერ იპოვის, აბრუნებს -1-ს











name = input("შეიყვანე შენი სახელი: ")


if name[0].isupper():
    print("Hello!")
else:
    print("Bye...")
    
    
    
    
    
    
    
    
    
    

name = input("შეიყვანე შენი სახელი: ")
surname = input("შეიყვანე შენი გვარი: ")


if surname[0].lower() == "m":
   
    print(surname.upper())
elif surname[0].lower() == "g":

    print(name.lower())
else:
    print("ვერ დაემთხვა არცერთი პირობა.")
    
    
    
    
    
    
    
    
    
    
    
color = input("შეიყვანე შენი საყვარელი ფერი: ")


if "p" in color.lower():
    print("Gamarjoba")
else:
    print("Naxvamdis")