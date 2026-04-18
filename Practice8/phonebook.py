#to connect Python to my PostgreSQL database
from connect import connect

# It searches contacts by a text pattern,The pattern can be part of a name or part of a phone number
def search_contacts(pattern):
    #open connection to the database
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM search_contacts(%s)", (pattern,))

    #fetch all rows returned by the SQL function
    rows = cur.fetchall()

    #Print results to the console
    print("\nSearch results:")
    for row in rows:
        print(row)
    cur.close()
    conn.close()

# It shows only part of the contacts table, limit = number of rows to show,offset = number of rows to skip
def show_paginated(limit, offset):
    #connect to database
    conn = connect()
    cur = conn.cursor()

    #call PostgreSQL FUNCTION with two parameters
    cur.execute("SELECT * FROM get_contacts_paginated(%s, %s)", (limit, offset))
    rows = cur.fetchall()
    print("\nPaginated results:")
    for row in rows:
        print(row)
    cur.close()
    conn.close()

#this function calls PostgreSQL PROCEDURE upsert_contact()
#"Upsert" means:if contact already exists - update
#if contact does not exist - insert new contact
def upsert_contact(name, phone):
    conn = connect()
    cur = conn.cursor()

    #CALL is used for procedures
    cur.execute("CALL upsert_contact(%s, %s)", (name, phone))
    conn.commit()
    print("Upsert done (insert or update).")
    cur.close()
    conn.close()


#this function calls PostgreSQL PROCEDURE delete_contact()
#it deletes a contact either by name or by phone
def delete_contact(name=None, phone=None):
    conn = connect()
    cur = conn.cursor()

    #call procedure with name and phone parameters
    #If one of them is None, PostgreSQL receives NULL
    cur.execute("CALL delete_contact(%s, %s)", (name, phone))
    #Save delete operation
    conn.commit()
    print("Delete done.")
    
    cur.close()
    conn.close()


# This function calls PostgreSQL PROCEDURE insert_many_contacts()
# It inserts several contacts at once, also validates phone numbers
def insert_many():
    conn = connect()
    cur = conn.cursor()
    #these lists will be sent to PostgreSQL as arrays
    names = ["Ali", "Aruzhan", "BadUser"]
    phones = ["87005553344", "87771236745", "123"]

    #Call stored procedure,PostgreSQL will check each phone number
    #Valid numbers will be inserted,Invalid numbers will show notice
    cur.execute(
        "CALL insert_many_contacts(%s, %s)",
        (names, phones)
    )
    conn.commit()
    print("Insert done")
    cur.close()
    conn.close()


#This is the main menu of the program,It lets the user choose what action to perform
def menu():
    while True:
        print("\n--- Practice 8 ---")
        print("1. Search contacts")
        print("2. Show paginated contacts")
        print("3. Upsert contact")
        print("4. Delete by name")
        print("5. Delete by phone")
        print("6. Insert many contacts")
        print("0. Exit")

        choice = input("Choose: ")

        #Option 1:search contacts
        if choice == "1":
            pattern = input("Enter search text: ")
            search_contacts(pattern)

        #Option 2:show contacts with pagination
        elif choice == "2":
            limit = int(input("Enter limit: "))
            offset = int(input("Enter offset: "))
            show_paginated(limit, offset)

        #Option 3:insert or update contact
        elif choice == "3":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            upsert_contact(name, phone)

        #Option 4:delete by name
        elif choice == "4":
            name = input("Enter name: ")
            delete_contact(name, None)

        #Option 5:delete by phone
        elif choice == "5":
            phone = input("Enter phone: ")
            delete_contact(None, phone)

        #Option 6:insert many contacts
        elif choice == "6":
            insert_many()

        #Option 0:exit program
        elif choice == "0":
            print("Bye")
            break


#This line checks if the file is run directly,If yes, it starts the menu
if __name__ == "__main__":
    menu()