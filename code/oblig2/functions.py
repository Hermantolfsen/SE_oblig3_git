#Oblig 2 Testing - Software Engineering og Testing - Herman Tolfsen
#Funksjon filen hvor man oppretter funksjoner

def is_leap_year(year):
   # Sjekker først om input er et tall
    if not isinstance(year, int):
        raise ValueError("Testen krever at man bruker et tall")


    if year % 4 == 0:
        if year % 100 == 0:
            return year % 400 == 0
        return True
    return False
