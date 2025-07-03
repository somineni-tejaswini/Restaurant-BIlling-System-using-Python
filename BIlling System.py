# ------------- MENU -------------
menu = {
  "ChickenBiryani": 300, "FishBiryani": 350, "MuttonBiryani": 400,
  "EggBiryani": 250, "PrawnBiryani": 310, "ChickenManchurian": 200,
  "ChickenCurry": 220, "MuttonCurry": 360, "PrawnCurry": 370, "ChickenFry": 280,
  "Chepatikurma": 100, "Vegetablepulao": 150, "ButterNaan": 152,
  "RumaalRoti": 120, "Paneer&Parota": 130, "PaneerBiryani": 200,
  "MushroomBiryani": 220, "PaneerTikka": 180, "GobiManchurian": 110,
  "CheesyPizza": 160
}

# ------------- DISPLAY MENU -------------
print("============== WELCOME TO PRIME RESTAURANT ==============")
print("                   Banjara Hills, Hyderabad")
print("---------------------------------------------------------")
print("| NON VEG ITEMS           | Price | VEG ITEMS           | Price |")
print("---------------------------------------------------------")

i = 0
nonveg = list(menu.items())[:10]
veg = list(menu.items())[10:]
while i < 10:
  left = nonveg[i][0].ljust(24) + "₹" + str(nonveg[i][1]).ljust(5)
  right = veg[i][0].ljust(22) + "₹" + str(veg[i][1]).ljust(5)
  print("| " + left + " | " + right + " |")
  i += 1
print("---------------------------------------------------------\n")

# ------------- BILL NUMBER -------------
billfile = "billno.txt"
try:
  f = open(billfile, "r")
  billno = int(f.read().strip())
  f.close()
except:
  billno = 100

try:
  f = open(billfile, "w")
  f.write(str(billno + 1))
  f.close()
except:
  print("❌ Failed to update bill number.")
  billno += 1

# ------------- ORDER INPUTS -------------
date = input("📅 Enter Date (DD/MM/YYYY): ")
table = input("🪑 Enter Table Number: ")
count = int(input("📝 Enter number of items: "))

item_list = []
qty_list = []
price_list = []
total_list = []

i = 0
while i < count:
  item = input("🍽️ Enter item name: ").strip()
  if item in menu:
    qty = input("🔢 Enter quantity for " + item + ": ")
    if qty.isdigit() and int(qty) > 0:
      qty = int(qty)
      price = menu[item]
      total = price * qty
      item_list.append(item)
      qty_list.append(qty)
      price_list.append(price)
      total_list.append(total)
      print("✅ Added:", item, "| Qty:", qty, "| Total: ₹", total, "\n")
      i += 1
    else:
      print("❌ Invalid quantity. Try again.\n")
  else:
    print("❌ Item not in menu. Try again.\n")

# ------------- PRINT FINAL BILL -------------
print("\n================== FINAL BILL ==================")
print("🧾 Bill No:", billno, "    🗓️ Date:", date, "    🪑 Table:", table)
print("------------------------------------------------")
print("Item".ljust(20) + "Qty".rjust(5) + "Price".rjust(10) + "Total".rjust(10))
print("------------------------------------------------")

i = 0
subtotal = 0
while i < count:
  subtotal += total_list[i]
  print(item_list[i].ljust(20), str(qty_list[i]).rjust(5), str(price_list[i]).rjust(10), str(total_list[i]).rjust(10))
  i += 1

tax = round(subtotal * 0.07, 2)
grand = round(subtotal + tax, 2)

print("------------------------------------------------")
print("Subtotal".ljust(35), "₹", subtotal)
print("GST (7%)".ljust(35), "₹", tax)
print("GRAND TOTAL".ljust(35), "₹", grand)
print("================================================")
print("🙏 Thank you! Visit Again.\n")
