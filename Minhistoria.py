hero_name = input("Vad heter hjälten? ")
hero_age = int(input("Hur gammal är hjälten? "))
hero_place = input("Var bor hjälten? ")
hero_item = input("Vilket föremål har hjälten? ")
gold = int(input("Hur många guldmynt har hjälten? "))
hero_health = 10

print("Det här är historien om", hero_name)
print("Hjälten är", hero_age, "år och bor i", hero_place)
print("Hjälten tar med sig", hero_item, "och ger sig ut på en resa.")

choice = input("Du hittar en gammal dörr. Vill du öppna den? (ja/nej): ")
if choice == "ja":
    gold = gold + 5
    hero_health = hero_health - 2
    print("Du hittar fem guldmynt men river dig på några taggar.")
    print("Du har", gold, "guldmynt och", hero_health, "hälsa.")
else:
    print("Du går förbi dörren.")

print("En handlare säljer ett svärd för 10 guldmynt. Du måste vara minst 18 år. ")
choice == input("Vill du köpa svärdet? "  "Ja eller Nej?: ")
if choice == "ja":
    if hero_item == "svärd":
        print("Du har redan ett svärd.")
    else:
        if hero_age >= 18 and gold >= 10:
            gold = gold - 10
            hero_item = "svärd"
            print("Du lämnar allt du hade och tar svärdet.")
            print("Du har", gold, "Guldmynt kvar")
    

