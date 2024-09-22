# Pizza Order Practice "Pizza Siparişi Uygulaması"

print("Welcome to python pizza Deliveries!")

# Kullanıcıdan pizza boyutunu alma
size = input("What size pizza do you want? S, M or L: ")
# Kullanıcıdan pepperoni isteğini alma
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
# Kullanıcıdan ekstra peynir isteğini alma
extra_cheese = input("Do you want extra cheese? Y or N: ")


# todo: work out how much they need to pay based on their size choice.

# Fatura başlangıç tutarını başlat
bill = 0

# Kullanıcının seçtiği pizza boyutuna göre fatura miktarını belirleme
if size == "S":
    bill += 15  # Küçük boy pizza ücreti

elif size == "M":
    bill += 20  # Orta boy pizza ücreti

elif size == "L":
    bill += 25  # Büyük boy pizza ücreti

else:
    print("You typed the wrong inputs.") # Geçersiz boyut girişi

# todo: work out how much to add to their bill based on their pepperoni choice.

# Kullanıcının pepperoni isteğine göre fatura miktarını artırma
if pepperoni == "Y":
    if size == "S":
        bill += 2 # Küçük pizza için pepperoni ücreti
    else:
        bill += 3 # Orta ve büyük pizza için pepperoni ücreti

# todo: work out their final amount based on whether if they want extra cheese. 

# Kullanıcının ekstra peynir isteğine göre fatura miktarını artırma 
if extra_cheese == "Y":
    bill += 1 # Ekstra peynir ücreti

# Sonuç olarak toplam fatura tutarını ekrana yazdırma
print(f"Your final bill is: ${bill}.")
