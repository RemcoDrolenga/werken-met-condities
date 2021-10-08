    #Remco Drolenga Solicitatie

Ervaring1 = int(input("Hoeveel jaar praktijk ervaring heeft u met Dieren-Dressuur? "))
Ervaring2 = int(input("Hoeveel jaar praktijk ervaring heeft u met Jongleren? "))
Ervaring3 = int(input("Hoeveel jaar praktijk ervaring heeft u met Acrobatiek? "))
DiplomaMBO4 = input("Bent u in bezit van een MBO-4 ondernemers diploma? J/N ")
Rijbewijs = input("Bent u in bezit van een geldig Vrachtwagen rijbewijs? J/N ")
Hoed = input("Bent u in bezit van een hoge hoed? J/N ")
BadSlipper = input("Heeft u rode Badslippers met oranje stippen? J/N ")
Telefoonhoesje = input("Zit er om uw telefoon een hoesje van Donald Duck? J/N ")
Tuinslang = input("Is uw tuinslang langer dan 30Meter? J/N ")
Nokia = input("Heeft u vroeger een nokia gehad? J/N ")
Geslacht = input("Bent u een man of vrouw? ")
if Geslacht == "man":
    Snor = input("Heeft u een snor? J/N ")
    if Snor == "ja":
        BreeteS = int(input("Hoe breed is uw snor? (In cm) "))
    else:
        BreeteS = 0
else:
    HaarK = input("Is uw haar rood krullend? J/N ")
    if HaarK == "ja":
        HaarL = int(input("Hoe lang is uw haar? (In cm) "))
    else:
        HaarL = 0
Lengte = int(input("Wat is uw lengte? (In cm) "))
Gewicht = int(input("Wat is uw gewicht? (In Kg) "))
Certificaat = input("Heeft u een certificaat: “Overleven met gevaarlijk personeel”? ")

if (Ervaring1 > 3 or Ervaring2 > 4 or Ervaring3 > 2) and DiplomaMBO4 == "ja" and Rijbewijs == "ja" and Hoed == "ja" and BadSlipper == "ja" and Telefoonhoesje == "ja" and Tuinslang == "ja" and Nokia == "ja" and (Geslacht == "man" and BreeteS > 9 or Geslacht == "vrouw" and HaarL > 19) and Lengte > 149 and Gewicht > 89 and Certificaat == "ja":
    print("Gefeliciteerd, u komt in aanmerking tot een solicitatie voor deze vacature. ")
else:
    print("Helaas, u komt niet in aanmerking tot een solicitatie voor deze vacature. ")




# if Ervaring1 > 3 or Ervaring2 > 4 or Ervaring3 > 2:
#     DiplomaMBO4 = input("Bent u in bezit van een MBO-4 ondernemers diploma? ")
#     if DiplomaMBO4 == "ja":
#         Rijbewijs = input("Bent u in bezit van een geldig Vrachtwagen rijbewijs? ")
#         if Rijbewijs == "ja":
#             Hoed = input("Bent u in bezit van een hoge hoed? ")
#             if Hoed == "ja":
#                 Geslacht = input("Bent u een man of vrouw? ")
#                 if Geslacht == "man":
#                     Snor = input("Heeft u een snor? ")
#                     if Snor == "ja":
#                         BreeteS = input("Hoe breed is uw snor? ")
#                         if BreeteS > "9":
#                             Lengte = input("Wat is uw lengte? (In cm) ")
#                             if Lengte > "149":
#                                 Gewicht = input("Wat is uw gewicht? ")
#                                 if Gewicht > "89":
#                                     Certificaat = input("Heeft u een certificaat 'Overleven met gevaarlijk personeel'? ")   
#                 else:
#                     HaarK = input("Is uw haar rood krullend? ")
#                     if HaarK == "ja":
#                         HaarL = input("Hoe lang is uw haar? ")
#                         if HaarL > "19":
#                             Lengte = input("Wat is uw lengte? (In cm) ")
#                             if Lengte > "149":
#                                 Gewicht = input("Wat is uw gewicht? ")
#                                 if Gewicht > "89":
#                                     Certificaat = input("Heeft u een certificaat 'Overleven met gevaarlijk personeel'? ")


