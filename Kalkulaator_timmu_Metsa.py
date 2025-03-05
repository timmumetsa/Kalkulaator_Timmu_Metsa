import math  # Impordib kõik matemaatikaga seonduvad funktsioonid.

class Calc:
    def __init__(self, num1, num2):
        self.a = num1
        self.b = num2

    def liitmine(self):                
        return self.a + self.b

    def lahutamine(self):               
        return self.a - self.b

    def korrutamine(self):              
        return self.a * self.b

    def jagamine(self): #
        if self.b != 0: # Kontroll jagamise nulliga vältimiseks.
            return self.a / self.b
        else:
            return "Viga: Nulliga jamine ei ole lubatud!" # Kuvab veateate, kui jagatakse nulliga.

    def jaak(self):
        if self.b != 0: # Kontroll nulliga jäägi vältimiseks.
            return self.a % self.b
        else:
            return "viga: Nulliga jäägi leidmine ei ole lubatud!"

    def aste(self): # Astendamine
        return self.a ** self.b

    def keskmine(self): # Lisatud keskmise leidmine.
        return (self.a + self.b) / 2

    def maksimum(self): # Lisatud maksimum väärtuse leidmine.
        return max(self.a, self.b)

def main(): # Kasutatud main() funktsiooni,et vältida globaalset koodi.
    try:
        a = int(input("Sisesta esimene number: "))
        b = int(input("Sisesta teine number: "))
    except ValueError: # Sisendi valideerimine, et kasutaja sisestaks ainult täisarvud.
        print("Viga: Palun sisesta ainult täisarvud!")
        return

    kalk = Calc(a, b) # test

    while True:
        print("\nValikud:")
        print("1. Liitmine")
        print("2. Lahutamine")
        print("3. Korrutamine")
        print("4. Jagamine")
        print("5. Jäägi Leidmine")
        print("6. Astendamine")
        print("7. Keskmise leidmine")
        print("8. Maksimumväärtuse Leidmine")
        print("9. Välju")
   # Lisatud selged valikud ja võimalus programmi lõpetamiseks.

        try:
            valik = int(input("Sisesta üks valikutest: "))
        except ValueError:
            print("Viga: Palun sisesta number vahemikus 1-9!") # Kui sisestatakse vale valik kuvatakse viga.
            continue

        if valik == 1:
            print("Vastus: ", kalk.liitmine())
        elif valik == 2:
            print("Vastus: ", kalk.lahutamine())
        elif valik == 3:
            print("Vastus: ", kalk.korrutamine())
        elif valik == 4:
            print("Vastus: ", kalk.jagamine())
        elif valik == 5:
            print("Vastus: ", kalk.jaak())
        elif valik == 6:
            print("Vastus: ", kalk.aste())
        elif valik == 7:
            print("Vastus: ", kalk.keskmine())
        elif valik == 8:
            print("Vastus: ", kalk.maksimum())
        elif valik == 9:
            print('Programmi lõpetamine.')
            break
        else:
            print("Viga: Paliun vali number 1-9!")

if __name__ == "__main__":
    main()




