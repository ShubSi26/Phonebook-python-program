import sqlite3
database=sqlite3.connect('phonbok.db')
try:
    database.execute("CREATE TABLE PHONEBOOK(Name,number,email)")
except:
    pass
def addcontact():
    print()
    name=input("Type name: ")
    number=input("Enter Number: ")
    email=input("Type email here: ")
    lst=str((name,number,email))
    txt="INSERT INTO PHONEBOOK(Name,number,email) VALUES"+lst
    database.execute(txt)
    database.commit()
    print("Added sucessfully")
def delcontact():
    name=input("Enter the name of address you want to delete: ")
    tl=database.execute("Select Name from PHONEBOOK")
    l = [a[0] for a in tl]
    if name in l:
        txt = "DELETE from PHONEBOOK where Name ='" + name + "'"
        database.execute(txt)
        database.commit()
        print("Removed succesfully")
    else:
        print("Not found")
def delallcontact():
    database.execute("DELETE from PHONEBOOK")
    database.commit()
    print("sucessfully deleted all contacts")
def srchforcontact():
    name=input("Enter the name you want to know the detail: ")
    tl = database.execute("Select Name from PHONEBOOK")
    l = [a[0] for a in tl]
    if name in l:
        txt="SELECT Name, number, email from PHONEBOOK where Name ='"+name+"'"
        lst=database.execute(txt)
        database.commit()
        for bb in lst:
            print("Name: ",bb[0])
            print("Number: ",bb[1])
            print("Email: ",bb[2])
    else:
        print("Not found")
def disallcntct():
    print()
    lst=database.execute("SELECT * FROM PHONEBOOK")
    database.commit()
    for c in lst:
        print("Name: ", c[0])
        print("Number: ", c[1])
        print("Email: ", c[2])
        print()
def pbupdate():
    name=input("Enter the contact name you want to update: ")
    tl = database.execute("Select Name from PHONEBOOK")
    l = [a[0] for a in tl]
    if name in l:
        number=input("Enter the updated number: ")
        email=input("Enter the updated email: ")
        txt="UPDATE PHONEBOOK set number="+str(number)+", email='"+email+"' WHERE Name='"+name+"'"
        database.execute(txt)
        database.commit()
        print("Updated Succesfully")
    else:
        print("Not found")
print("Welcome to your phonebook")
a=input("Please press enter to continue")
tr=True
while tr:
    print("\tYou can now perform the following operations on this phonebook\n")
    print("1. Add a new contact")
    print("2. Remove an existing contact")
    print("3. Delete all contacts")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Update a contact")
    print("7. Exit phonebook")
    inp = input("Type your input here: ")
    if inp=="1":
        addcontact()
    elif inp=="2":
        delcontact()
    elif inp=="3":
        delallcontact()
    elif inp=="4":
        srchforcontact()
    elif inp=="5":
        disallcntct()
    elif inp=="6":
        pbupdate()
    elif inp=="7":
        break
    else:
        print("Please enter corret input")
        h = input("Press enter to continue")
        continue
    h=input("Press enter to continue")
print()
print("Thankyou for using Phonebook Program")
print("Phonebook program ended")
database.close()
