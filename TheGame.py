#Remco Drolenga: KaasKaasEnNogIsKaas

Keuze1 = input("Je ziet een eiland, vaar je naar het eiland toe? ja/nee ")
if Keuze1 == "ja":
    keuze2 = input("Je ziet op het eiland een lang strand en een dicht begroeid bos. Ga je het bos in? ja/nee ")
    if keuze2 == "ja":
        keuze3 = input("Je gaat het bos in, hier kom je fel rode besjes tegen, je hebt verschrikkelijke trek. Eet je de besjes of loop je door? ja/nee ")
        if keuze3 == "ja":
            print("De besjes bleken giftige besjes te zijn. Je sterft door het eten van de besjes.")
        else:
            keuze4 = input("Je bent langs de besjes gelopen, een kleine 10 minuten later kom je een klein huisje tegen. Ga je bij het huisje naar binnen? ja/nee ")
            if keuze4 == "ja":
                 keuze5 = input("Je probeert het huisje open te maken, hij zit alleen op slot. Ga je opzoek naar de sleutel? ja/nee ")
                 if keuze5 == "ja":
                    keuze6 = input("Je kijkt bij het huisje en vind uiteindelijk geen sleutel. Je zou de deur in kunnen trappen. ja/nee ")
                    if keuze6 == "ja":
                        print("Je trapt de deur in, dit maakt een behoorlijk lawaai. Waardoor je de aandacht trekt van een aantal inboorlingen die iets verderop in de bosjes wonen. De aanval van hun overleef je helaas niet.")
                    else:
                        print("Je zoekt nog even verder en het valt je opeens op dat er een klein raampje ergens open staat, je kruipt daardoor naar binnen en komt een kaart tegen met een route naar een ander huisje verderop waar een bootje naast lijkt te liggen. Je volgt de route en je vaart je vrijheid te gemoed.")
                 else:
                    vraag7 = input("je vind het niet de moeite waard en loopt verder, opzoek naar een slaapplaats. je vind na een tijdje een grot. Ga je hier de nacht doorbrengen? ja/nee ")
                    if vraag7 == "ja":
                        print("Je hebt er voor gekozen om de grot in te lopen. Hier kom je midden in de nacht een grote beer tegen..")
                    else:
                        print("Je bent doorgelopen op zoek naar een andere slaapplaats, alleen kun je niks beters vinden dan een hoge boom. Je klimt in de boom en gaat liggen en zit dan oog in oog met een giftige slang.")
            else:
                keuze8 = input("Je loopt verder, en iets verderop hoor je wat geritsel in de bosjes rechts van je, ga je kijken wat er in de bosjes zit? ja/nee ")
                if keuze8 == "ja":
                    print("je gaat kijken bij het bosje, alleen in het bosje blijkt een grote tijger te zitten te zitten die je bespringt en opeet.")
                else:
                    vraag9 = input("Je loopt dieper en dieper het bos in, totdat je bij een berg en een strandje. Ga je de berg omhoog? ja/nee ")
                    if vraag9 == "ja":
                        print("Je loopt de berg op, om er vervolgens achter te komen dat er niks te zoeken is, en op je weg terug naar beneden rolt er een steen onder je voet weg en val je naar beneden.")
                    else:
                        print("je komt een strandje tegen, bij het strandje staat er een huisje met een klein bootje ernaast, je loopt het huisje in om te zoeken naar wat eten en brandstof. Dit kun je allebei vinden. Je vaart weg van het eiland in het bootje.")