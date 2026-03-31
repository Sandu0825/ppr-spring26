import csv
from connect import connect


def create_table():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(100) NOT NULL,
            phone VARCHAR(20) NOT NULL UNIQUE
        )
    """)

    conn.commit()
    cur.close()
    conn.close()
    print("Table is ready.")


def insert_contact(first_name, phone):
    conn = connect()
    cur = conn.cursor()

    try:
        cur.execute(
            "INSERT INTO contacts (first_name, phone) VALUES (%s, %s)",
            (first_name, phone)
        )
        conn.commit()
        print("Contact added successfully.")
    except Exception as e:
        conn.rollback()
        print("Error while adding contact:", e)

    cur.close()
    conn.close()


def insert_from_csv(file_name):
    conn = connect()
    cur = conn.cursor()

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                cur.execute(
                    """
                    INSERT INTO contacts (first_name, phone)
                    VALUES (%s, %s)
                    ON CONFLICT (phone) DO NOTHING
                    """,
                    (row["first_name"], row["phone"])
                )

        conn.commit()
        print("CSV data imported successfully.")
    except Exception as e:
        conn.rollback()
        print("Error while importing CSV:", e)

    cur.close()
    conn.close()


def get_all_contacts():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM contacts ORDER BY id")
    rows = cur.fetchall()

    if not rows:
        print("No contacts found.")
    else:
        print("\nAll contacts:")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}")

    cur.close()
    conn.close()


def search_by_name(name):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM contacts WHERE first_name ILIKE %s ORDER BY id",
        ("%" + name + "%",)
    )
    rows = cur.fetchall()

    if not rows:
        print("No matching contacts found.")
    else:
        print("\nSearch results:")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}")

    cur.close()
    conn.close()


def search_by_phone_prefix(prefix):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM contacts WHERE phone LIKE %s ORDER BY id",
        (prefix + "%",)
    )
    rows = cur.fetchall()

    if not rows:
        print("No matching contacts found.")
    else:
        print("\nSearch results:")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}")

    cur.close()
    conn.close()


def update_name_by_phone(phone, new_name):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "UPDATE contacts SET first_name = %s WHERE phone = %s",
        (new_name, phone)
    )

    if cur.rowcount == 0:
        print("No contact found with this phone.")
    else:
        conn.commit()
        print("Name updated successfully.")

    cur.close()
    conn.close()


def update_phone_by_name(first_name, new_phone):
    conn = connect()
    cur = conn.cursor()

    try:
        cur.execute(
            "UPDATE contacts SET phone = %s WHERE first_name = %s",
            (new_phone, first_name)
        )

        if cur.rowcount == 0:
            print("No contact found with this name.")
        else:
            conn.commit()
            print("Phone updated successfully.")
    except Exception as e:
        conn.rollback()
        print("Error while updating phone:", e)

    cur.close()
    conn.close()


def delete_by_name(first_name):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM contacts WHERE first_name = %s",
        (first_name,)
    )

    if cur.rowcount == 0:
        print("No contact found with this name.")
    else:
        conn.commit()
        print("Contact deleted successfully.")

    cur.close()
    conn.close()


def delete_by_phone(phone):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM contacts WHERE phone = %s",
        (phone,)
    )

    if cur.rowcount == 0:
        print("No contact found with this phone.")
    else:
        conn.commit()
        print("Contact deleted successfully.")

    cur.close()
    conn.close()


def menu():
    while True:
        print("\n--- PHONEBOOK MENU ---")
        print("1. Create table")
        print("2. Insert contact from console")
        print("3. Import contacts from CSV")
        print("4. Show all contacts")
        print("5. Search by name")
        print("6. Search by phone prefix")
        print("7. Update name by phone")
        print("8. Update phone by name")
        print("9. Delete by name")
        print("10. Delete by phone")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_table()

        elif choice == "2":
            first_name = input("Enter name: ")
            phone = input("Enter phone: ")
            insert_contact(first_name, phone)

        elif choice == "3":
            file_name = input("Enter CSV file name: ")
            insert_from_csv(file_name)

        elif choice == "4":
            get_all_contacts()

        elif choice == "5":
            name = input("Enter name to search: ")
            search_by_name(name)

        elif choice == "6":
            prefix = input("Enter phone prefix: ")
            search_by_phone_prefix(prefix)

        elif choice == "7":
            phone = input("Enter current phone: ")
            new_name = input("Enter new name: ")
            update_name_by_phone(phone, new_name)

        elif choice == "8":
            first_name = input("Enter current name: ")
            new_phone = input("Enter new phone: ")
            update_phone_by_name(first_name, new_phone)

        elif choice == "9":
            first_name = input("Enter name to delete: ")
            delete_by_name(first_name)

        elif choice == "10":
            phone = input("Enter phone to delete: ")
            delete_by_phone(phone)

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    menu()