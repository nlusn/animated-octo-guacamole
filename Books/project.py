import psycopg2
from datetime import date

# --- Database connection ---
conn = psycopg2.connect(
    dbname="fitness_db",
    user="postgres",
    password="yourpassword",
    host="localhost",
    port="5432"
)
cur = conn.cursor()


# --- Add a new member ---
def add_member():
    print("=== Add Member ===")
    first = input("First Name: ")
    last = input("Last Name: ")
    dob = input("Date of Birth (YYYY-MM-DD): ")
    gender = input("Gender (Male/Female/Other): ")
    email = input("Email: ")
    phone = input("Phone Number: ")
    address = input("Address: ")
    membership = input("Membership Type (Standard/Premium/VIP): ")
    join_date = date.today()
    expiry_date = date(join_date.year + 1, join_date.month, join_date.day)

    cur.execute("""
        INSERT INTO Members (FirstName, LastName, DateOfBirth, Gender, Email, PhoneNumber, Address, MemberShipType, JoinDate, ExpiryDate)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (first, last, dob, gender, email, phone, address, membership, join_date, expiry_date))
    conn.commit()
    print("✅ Member added successfully.\n")


# --- View all members ---
def view_members():
    print("=== Members List ===")
    cur.execute("SELECT MemberID, FirstName, LastName, Email FROM Members")
    rows = cur.fetchall()
    for row in rows:
        print(f"{row[0]}: {row[1]} {row[2]} | {row[3]}")
    print()


# --- Make a payment ---
def make_payment():
    print("=== Make Payment ===")
    member_id = input("Member ID: ")
    class_id = input("Class ID: ")
    enroll_date = date.today()
    end_date = date(enroll_date.year, enroll_date.month + 1, enroll_date.day)
    method = input("Payment Method (Cash/Card/Transfer): ")

    cur.execute("""
        INSERT INTO Payments (MemberID, ClassID, EnrollDate, EndDate, PaymentMethod)
        VALUES (%s, %s, %s, %s, %s)
    """, (member_id, class_id, enroll_date, end_date, method))
    conn.commit()
    print("✅ Payment recorded.\n")


# --- Menu ---
def menu():
    while True:
        print("=== Fitness Center Console App ===")
        print("1. Add Member")
        print("2. View Members")
        print("3. Make Payment")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_member()
        elif choice == "2":
            view_members()
        elif choice == "3":
            make_payment()
        elif choice == "4":
            break
        else:
            print("❌ Invalid choice.\n")

    cur.close()
    conn.close()
    print("Bye! 👋")

menu()
