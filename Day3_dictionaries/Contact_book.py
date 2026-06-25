contacts ={}
def add_contact(): 
    name = input("enter your name: ")
    contact = input("enter your contact details:")
    email = input("enter your email details: ")
    contact[name] = {
        "phone":phone,
        "email":email
    }
    print("👍contact added successfully")
def search_contact():
    name = input("entre the contacts")
    contact=contacts.get(name)
    if contact:
        print("phone: ",contact.get("phone"))
        print("email: ",contact.get("email"))
    else:
        print("contact not found please try agian later")
def update_contact():
    name = input("enter your name")
    contact = contacts.get(name)
    if contact:
        new_phone = input("enter your new phone number: ")
        new_email = input("enter ypur new email id: ")
        contact.update({
            "phone": new_phone,
            "email":new_email
        })
        print("contact updated successfully")
    else:
        print("invalid entry!contact not found please try agin later")
def delete_contact():
    name = input("enter your name to delete: ")
    contact=contacts.get(name)
    if name in contacts:
        contact.pop(name)
        print("contact deleted successfully")
    else:
        print("rocess not done please try agin later")
def view_contact():
    if not contacts:
        print("sorry contact not found please try agin later")
    else:
        for name,details in contact.items():
            print(f"""
                  name:{name}
                  phone:{details['phone']}
                  email:{details['email']}============="""
                  )
def show_dictionary_methods():
    print("KEYS: " ,list(contacts.keys()))
    print("VALUES: ",list(contacts.value()))
    print("items: ",list(contcats.items()))
while True:
    print("""====THE CONTACT BOOK📖=====
1.add contacts
2.search contacts
3.update contacts
4.delete contacts
5.view contacts
6.show dictionary show_dictionary_methods
7.exit """)
    choice = input("enter your choice :")
    if(choice == 1):
        print("add contcats",add_contact)
    elif(choice == 2):
        print("search contacts",search_contact)
    elif(choice == 3):
        print("update contacts",update_contact)
    elif(choice == 4):
        print("delete contacts",delete_contact)
    elif(choice == 5):
        print("view contacts",view_contact)
    elif(choice == 6):
        print("python dictionaries",show_dictionary_methods)
    else:
        print("you entered an invlaid choice try again later")




    



    
    

