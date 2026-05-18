def load_reservations(filename="reservations.txt"):
    reservations = []
    try:
        with open(filename, "r") as file:
            for line in file:
                table, date, time, name = line.strip().split(",")
                reservations.append({
                    "table": int(table),
                    "date": date,
                    "time": time,
                    "name": name
                })
    except FileNotFoundError:
        pass  # File doesn't exist yet
    return reservations


def save_reservation(table, date, time, name, filename="reservations.txt"):
    with open(filename, "a") as file:
        file.write(f"{table},{date},{time},{name}\n")


def book_table():
    table = int(input("Table number: "))
    date = input("Date (YYYY-MM-DD): ")
    time = input("Time (HH:MM): ")
    name = input("Customer name: ")

    reservations = load_reservations()

    # Check for double booking
    for r in reservations:
        if r["table"] == table and r["date"] == date and r["time"] == time:
            print("❌ This table is already booked for that date and time.")
            return

    # If free, save it
    save_reservation(table, date, time, name)
    print("✅ Reservation added successfully!")


# Run the system
book_table()
