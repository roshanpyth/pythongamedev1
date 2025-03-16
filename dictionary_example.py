country_dict={}
while True:
    print("1.Insert")
    print("2.Display all countries")
    print("3.Display all capitals")
    print("4.Get capital")
    print("5.Delete")
    choice=input("Enter the choice (1-5)")
    if choice=="1":
        country=input("Enter the country")
        capital=input("Enter the capital")
        country_dict[country]=capital
    elif choice=="2":
        print(country_dict.keys())
    elif choice=="3":
        country_dict.values
    elif choice=="4":
        country_dict[country]=capital
    elif choice=="5":
        country=input("Enter the country name")
        del country_dict[country]
        print(country_dict)
    else:
        print("Enter valid number")
        break

        






