contacts={}
while True:
    print("Hello, Welcome to my contact book App")
    print("1. Create")
    print("2.View")
    print("3.Update")
    print("4.Delete")
    print("5.Search")
    print("6.Count")
    print("7.Exit")
    try:
       choice=int(input("enter you choice:"))
    except ValueError:
        print("invalid input. Please enter a number ")
        continue

    if choice==1:
        name=input("Enter name:")
        if name in contacts:
            print(f"constact {name} is already exist")
        else:
            age=input("enter  age:")
            Email=input("enter   Email:")
            phoneNO=input("enter contact:")
            contacts[name]={'age':int(age),"email":Email,"PhoneNO":int(phoneNO)}
            print(f"contact name {name} has been  created successfully!")
            
    elif choice==2:
        name=input("enter the name to view the detail:")
        if name in contacts:
            print(f"age:{contacts[name]['age']}, email: {contacts[name]['email']}, PhoneNo: {contacts[name]['PhoneNO']}")

        else:
            print(f"contact Name {name} is not found:")

    elif choice==3:
        name=input("Enter the name to update the data:")
        if name in contacts:
            age=input("enter updated age=:")
            Email=input('enter updated email=:')
            phoneNO=input("enter updated phoneNo:=")
            contacts[name]={'age':int(age),"email":Email,"PhoneNO":int(phoneNO)}
        else:
            print("name is not found:")

    elif choice==4:
        name=input("Enter contact name to delete:=")
        if name in contacts:
            del contacts[name]
            print(f"contact name {name} is successfully deleted")
        else:
            print(f"contact name{name} is not found")

    elif choice==5:
        Search_name=input("enter contact name to search:=")
        found=False
        for name,contact in contacts.items():
            if Search_name.lower() in name.lower():
             print(f"Found - Name: {name}, Age: {contact['age']}, Email: {contact['email']}, PhoneNo: {contact['PhoneNO']}")
             found=True
        if not found:
            print("contact is not found in this name:")

    elif choice==6:
        print(f'Total contact in this you contacts book {len(contacts)}')
        print(contacts)

    elif choice==7:
        print("Good bye... closing the program 'Thank you For using this App'\n")
        break
    else:
        print('invalid input please enter valid choice:')
