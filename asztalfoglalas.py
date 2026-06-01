from datetime import datetime

def foglalasok_betoltese(filename="reservations.txt"):
   foglalasok = []
   try:
       with open(filename, "r") as file:
           for sor in file:
               asztal, datum, ido, nev = sor.strip().split(",")
               foglalasok.append({
                   "asztal": int(asztal),
                   "datum": datum,
                   "ido": ido,
                   "nev": nev
               })
   except FileNotFoundError:
       pass
   return foglalasok


def foglalas_mentese(asztal, datum, ido, nev, filename="reservations.txt"):
   with open(filename, "a") as file:
       file.write(f"{asztal},{datum},{ido},{nev}\n")


nyitvatartas = {
   "Hetfo": [("08:00", "10:30"), ("13:00", "16:30"), ("20:00", "02:00")],
   "Kedd": [("08:00", "10:30"), ("13:00", "16:30"), ("20:00", "02:00")],
   "Szerda": [("08:00", "10:30"), ("13:00", "16:30"), ("20:00", "02:00")],
   "Csutortok": [("08:00", "10:30"), ("13:00", "16:30"), ("20:00", "02:00")],
   "Pentek": [("08:00", "10:30"), ("13:00", "16:30"), ("20:00", "02:00")],
   "Szombat": [("08:00", "10:30"), ("13:00", "16:30"), ("20:00", "02:00")],
   "Vasarnap": [("08:00", "10:30"), ("13:00", "16:30"), ("20:00", "02:00")]
}

def nyitva_van(nap_nev, ido_str):
   if nap_nev not in nyitvatartas:
       return False
   ido_obj = datetime.strptime(ido_str, "%H:%M")
   for kezdet, veg in nyitvatartas[nap_nev]:
       kezdet_obj = datetime.strptime(kezdet, "%H:%M")
       veg_obj = datetime.strptime(veg, "%H:%M")

       if veg_obj < kezdet_obj:
           if ido_obj >= kezdet_obj or ido_obj <= veg_obj:
               return True
       else:
           if kezdet_obj <= ido_obj <= veg_obj:
               return True
   return False


def asztal_foglalas():

   while True:
       try:
           asztal = int(input("Asztal száma (1-20): "))
           if 1 <= asztal <= 20:
               break
           print("Az asztalszám 1 és 20 között lehet!")
       except ValueError:
           print("Számot adj meg!")

   while True:
       datum = input("Dátum (YYYY-MM-DD): ")
       try:
           datetime.strptime(datum, "%Y-%m-%d")
           break
       except ValueError:
           print("Hibás dátum!")
  
   while True:
       ido = input("Idő (HH:MM): ")
       try:
           datetime.strptime(ido, "%H:%M")
           break
       except ValueError:
           print("Hibás idő!")

   while True:
       nev = input("Foglaló neve: ").strip()
       if nev:
           break
       print("A név nem lehet üres!")
  
   napok_magyarul = {
       "Monday": "Hetfo",
       "Tuesday": "Kedd",
       "Wednesday": "Szerda",
       "Thursday": "Csutortok",
       "Friday": "Pentek",
       "Saturday": "Szombat",
       "Sunday": "Vasarnap"
   }
   angol_nap = datetime.strptime(datum, "%Y-%m-%d").strftime("%A")
   nap_nev = napok_magyarul[angol_nap]

   if not nyitva_van(nap_nev, ido):
       print("Ebben az időpontban zárva vagyunk.")
       print("Nyitvatartás:")
       for kezdet, veg in nyitvatartas[nap_nev]:
           print(f" - {kezdet} - {veg}")
       return
   
   foglalasok = foglalasok_betoltese()

   for f in foglalasok:
       if f["asztal"] == asztal and f["datum"] == datum and f["ido"] == ido:
           print("❌ Ez az asztal erre az időpontra már foglalt.")
           return
   
   foglalas_mentese(asztal, datum, ido, nev)
   print("Sikeres foglalás!")

asztal_foglalas()
