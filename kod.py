from datetime import datetime

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
        pass  
    return reservations


def save_reservation(table, date, time, name, filename="reservations.txt"):
    with open(filename, "a") as file:
        file.write(f"{table},{date},{time},{name}\n")


opening_hours = {
    "Hetfo": [("08:00", "10:30"), ("13:00", "16:30"), ("20:00", "02:00")],
    "Kedd": [("08:00", "10:30"), ("13:00", "16:30"), ("20:00", "02:00")],
    "Szerda": [("08:00", "10:30"), ("13:00", "16:30"), ("20:00", "02:00")],
    "Csutortok": [("08:00", "10:30"), ("13:00", "16:30"), ("20:00", "02:00")],
    "Pentek": [("08:00", "10:30"), ("13:00", "16:30"), ("20:00", "02:00")],
    "Szombat": [("08:00", "10:30"), ("13:00", "16:30"), ("20:00", "02:00")],
    "Vasarnap": [("08:00", "10:30"), ("13:00", "16:30"), ("20:00", "02:00")]
}


def is_open(day_name, time_str):
    if day_name not in opening_hours:
        return False

    time_obj = datetime.strptime(time_str, "%H:%M")

    for start, end in opening_hours[day_name]:
        start_obj = datetime.strptime(start, "%H:%M")
        end_obj = datetime.strptime(end, "%H:%M")

        if end_obj < start_obj:
            if time_obj >= start_obj or time_obj <= end_obj:
                return True
        else:
            if start_obj <= time_obj <= end_obj:
                return True

    return False


def book_table():
    table = int(input("Asztal száma: "))
    date = input("Dátum (éééé-hh-nn): ")
    time = input("Idő (óó:pp): ")

    days_hu = {
        "Monday": "Hetfo",
        "Tuesday": "Kedd",
        "Wednesday": "Szerda",
        "Thursday": "Csutortok",
        "Friday": "Pentek",
        "Saturday": "Szombat",
        "Sunday": "Vasarnap"
    }

    weekday_en = datetime.strptime(date, "%Y-%m-%d").strftime("%A")
    day_name = days_hu[weekday_en]

    if not is_open(day_name, time):
        print("Ebben az időpontban zárva vagyunk.")
        print("Nyitvatartási sávok ezen a napon:")
        for s, e in opening_hours[day_name]:
            print(f" - {s} - {e}")
        return

    name = input("Foglaló neve: ")

    reservations = load_reservations()

    for r in reservations:
        if r["table"] == table and r["date"] == date and r["time"] == time:
            print("Ez az asztal erre az időpontra le van foglalva.")
            return

    save_reservation(table, date, time, name)
    print("Sikeres foglalás!")


book_table()
