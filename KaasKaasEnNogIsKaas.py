#Remco Drolenga: KaasKaasEnNogIsKaas

Vraag1 = input("Is de kaas geel? ")
if Vraag1 == "ja":
    Vraag2 = input("Zitten er gaten in de kaas? ")
    if Vraag2 == "ja":
        Vraag3 = input("Is de kaas belachelijk duur? ")
        if Vraag3 == "ja":
            print("Dan is de kaas Emmenthaler.")
        else:
            print("Dan is de kaas Leerdammer.")
    else:
        Vraag4 = input("Is de kaas hard als steen? ")
        if Vraag4 == "ja":
            print("Dan is de kaas Pannigiano Reggiono.")
        else:
            print("Dan is de kaas Goudse Kaas.")
else:
    Vraag5 = input("Heeft de kaas blauwe schimmels? ")
    if Vraag5 == "ja":
        Vraag6 = input("Heeft de kaas een korst? ")
        if Vraag6 == "ja":
            print("Dan is de kaas Blue de Rochbaron.")
        else:
            print("Dan is de kaas Foume d'Ambert.")
    else:
        vraag7 =  input("Heeft de kaas een korst? ")
        if vraag7 == "ja":
            print("Dan is de kaas Camembert.")
        else:
            print("Dan is de kaas Mozzeralla.")