import json
from connect import get_connection


# -------- SHOW ALL CONTACTS --------
def show_contacts():
    """
    This function displays all contacts from the database.
    It joins contacts, groups, and phones tables.
    """

    conn = get_connection()  # open connection to database
    cur = conn.cursor()      # create cursor to execute SQL queries

    # SQL query with JOINs to get full information
    cur.execute("""
        SELECT c.first_name, c.last_name, c.email, g.name, p.phone, p.type
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
        LEFT JOIN phones p ON c.id = p.contact_id
        ORDER BY c.first_name;
    """)

    rows = cur.fetchall()  # get all results

    # print each row
    for row in rows:
        print(row)

    cur.close()
    conn.close()


# -------- SEARCH FUNCTION --------
def search():
    """
    This function searches contacts using the SQL function search_contacts().
    It matches name, email, and phone.
    """

    query = input("Enter search text: ")

    conn = get_connection()
    cur = conn.cursor()

    # calling SQL function from procedures.sql
    cur.execute("SELECT * FROM search_contacts(%s);", (query,))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


# -------- FILTER BY GROUP --------
def filter_group():
    """
    Shows only contacts from a selected group.
    Example: Family, Work, Friend
    """

    group = input("Enter group name: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT c.first_name, c.last_name, g.name
        FROM contacts c
        JOIN groups g ON c.group_id = g.id
        WHERE g.name ILIKE %s;
    """, (group,))

    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()


# -------- ADD PHONE --------
def add_phone():
    """
    Calls stored procedure add_phone.
    Adds a new phone number to existing contact.
    """

    name = input("Enter contact name: ")
    phone = input("Enter phone: ")
    p_type = input("Type (home/work/mobile): ")

    conn = get_connection()
    cur = conn.cursor()

    # call PostgreSQL procedure
    cur.execute("CALL add_phone(%s, %s, %s);", (name, phone, p_type))

    conn.commit()  # save changes
    cur.close()
    conn.close()

    print("Phone added successfully!")


# -------- MOVE TO GROUP --------
def move_group():
    """
    Moves contact to another group.
    If group does not exist, it will be created.
    """

    name = input("Enter contact name: ")
    group = input("Enter new group: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("CALL move_to_group(%s, %s);", (name, group))

    conn.commit()
    cur.close()
    conn.close()

    print("Contact moved!")


# -------- EXPORT TO JSON --------
def export_json():
    """
    Exports all contacts to JSON file.
    """

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT c.first_name, c.last_name, c.email, g.name, p.phone, p.type
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
        LEFT JOIN phones p ON c.id = p.contact_id;
    """)

    rows = cur.fetchall()

    data = []

    # convert SQL rows to JSON structure
    for row in rows:
        data.append({
            "first_name": row[0],
            "last_name": row[1],
            "email": row[2],
            "group": row[3],
            "phone": row[4],
            "type": row[5]
        })

    # write to file
    with open("contacts.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    cur.close()
    conn.close()

    print("Exported to contacts.json")


# -------- IMPORT FROM JSON --------
def import_json():
    """
    Imports contacts from JSON file.
    If contact already exists, user chooses skip or overwrite.
    """

    conn = get_connection()
    cur = conn.cursor()

    with open("contacts.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    for item in data:
        name = item["first_name"]
        email = item.get("email")

        # check if contact exists
        cur.execute("SELECT id FROM contacts WHERE first_name=%s", (name,))
        existing = cur.fetchone()

        if existing:
            choice = input(f"{name} exists. skip/overwrite: ")

            if choice == "skip":
                continue
            elif choice == "overwrite":
                cur.execute("""
                    UPDATE contacts
                    SET email=%s
                    WHERE first_name=%s
                """, (email, name))
        else:
            cur.execute("""
                INSERT INTO contacts(first_name, email)
                VALUES (%s, %s)
            """, (name, email))

    conn.commit()
    cur.close()
    conn.close()

    print("Import finished!")


# -------- PAGINATION --------
def paginate():
    """
    Shows contacts in pages using LIMIT/OFFSET.
    User can navigate with next/prev.
    """

    limit = 3
    offset = 0

    conn = get_connection()
    cur = conn.cursor()

    while True:
        cur.execute("""
            SELECT first_name, last_name
            FROM contacts
            ORDER BY id
            LIMIT %s OFFSET %s;
        """, (limit, offset))

        rows = cur.fetchall()

        if not rows:
            print("No more data")
            break

        for row in rows:
            print(row)

        action = input("next / prev / quit: ")

        if action == "next":
            offset += limit
        elif action == "prev":
            offset = max(0, offset - limit)
        elif action == "quit":
            break

    cur.close()
    conn.close()

def sort_contacts():
    print("Sort by: name / birthday / date")
    field = input("Choose: ").lower()

    conn = get_connection()
    cur = conn.cursor()

    if field == "name":
        cur.execute("SELECT first_name, last_name FROM contacts ORDER BY first_name;")
    elif field == "birthday":
        cur.execute("SELECT first_name, birthday FROM contacts ORDER BY birthday;")
    elif field == "date":
        cur.execute("SELECT first_name, created_at FROM contacts ORDER BY created_at;")
    else:
        print("Wrong option")
        return

    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()


# -------- MENU --------
def menu():
    """
    Main console menu.
    """

    while True:
        print("""
1. Show contacts
2. Search
3. Filter by group
4. Add phone
5. Move to group
6. Export JSON
7. Import JSON
8. Pagination
9. Sorted
0. Exit
""")

        choice = input("Choose option: ")

        if choice == "1":
            show_contacts()
        elif choice == "2":
            search()
        elif choice == "3":
            filter_group()
        elif choice == "4":
            add_phone()
        elif choice == "5":
            move_group()
        elif choice == "6":
            export_json()
        elif choice == "7":
            import_json()
        elif choice == "8":
            paginate()
        elif choice == "9":
            sort_contacts()
        elif choice == "0":
            break
        else:
            print("Invalid choice")


# program starts here
if __name__ == "__main__":
    menu()