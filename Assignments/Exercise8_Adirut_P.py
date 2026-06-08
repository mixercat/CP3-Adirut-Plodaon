Username = input("Enter your username: ")
Password = input("Enter your password: ")

if Username == "admin" and Password == "1234":
    print("Welcome admin to the mall!")
    current_user = "admin"
elif Username == "Customer" and Password == "1234":
    print("Welcome Customer to the mall!")
    current_user = "Customer"
else:
    print("Invalid username or password. Please try again.")
    current_user = "Error"


if current_user == "admin":
    print("-------------------------------------------")
    print("Banana     : 10      Baht", "Stock : 100")
    print("Apple      : 20      Baht", "Stock : 200")
    print("Orange     : 15      Baht", "Stock : 150")
    print("Computer   : 15000   Baht", "Stock : 50")
    print("GPU        : 30000   Baht", "Stock : 25")
    print("CPU        : 20000   Baht", "Stock : 30")
    print("Cooler     : 5000    Baht", "Stock : 100")
    print("RAM        : 8000    Baht", "Stock : 200")
    print("SSD        : 4000    Baht", "Stock : 150")
    print("HDD        : 3000    Baht", "Stock : 100")
    print("-------------------------------------------")
elif current_user == "Customer":
    print("-------------------------------------------")
    print("Banana     : 10      Baht")
    print("Apple      : 20      Baht")
    print("Orange     : 15      Baht")
    print("Computer   : 15000   Baht")
    print("Gpu        : 30000   Baht")
    print("Cpu        : 20000   Baht")
    print("Cooler     : 5000    Baht")
    print("Ram        : 8000    Baht")
    print("Ssd        : 4000    Baht")
    print("Hdd        : 3000    Baht")
    print("-------------------------------------------")
    Banana = 10
    Apple = 20
    Orange = 15
    Computer = 15000
    Gpu = 30000
    Cpu = 20000
    Cooler = 5000
    Ram = "Out Stock"
    Ssd = "Out Stock"
    Hdd = "Out Stock"
    print("Which product are you interested in buying?")
    print("-------------------------------------------")
    current_price = 0
    Vat = 7/100
    while True:
        user_choice = input("Which product are you interested in buying? : ")
    
        if user_choice == "Stop":
            print("VAT 7%")
            print("-------------------------------------------")
            print("Total price is : ", (current_price * Vat) + current_price , "Bath")
            print("Thank you!")
            print("-------------------------------------------")
            break     
        elif user_choice == "Banana":
            print("Price of Banana is :", Banana, "Baht")
            current_price += Banana       
        elif user_choice == "Apple":
            print("Price of Apple is :", Apple, "Baht")
            current_price += Apple        
        elif user_choice == "Orange":
            print("Price of Orange is :", Orange, "Baht")
            current_price += Orange        
        elif user_choice == "Computer":
            print("Price of Computer is :", Computer, "Baht")
            current_price += Computer        
        elif user_choice == "Gpu":
            print("Price of Gpu is :", Gpu, "Baht")
            current_price += Gpu        
        elif user_choice == "Cpu":
            print("Price of Cpu is :", Cpu, "Baht")
            current_price += Cpu       
        elif user_choice == "Cooler":
            print("Price of Cooler is :", Cooler, "Baht")
            current_price += Cooler        
        elif user_choice == "Ram":
            print("Ram is :", Ram)        
        elif user_choice == "Ssd":
            print("Ssd is :", Ssd)       
        elif user_choice == "Hdd":
            print("Hdd is :", Hdd)       
        else:
            print("Sorry, we don't have this product.")