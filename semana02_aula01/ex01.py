'''1) Considere as variáveis abaixo, inicializadas como segue:
a) numero1 = 300
b) numero2 = 100
c) numero3 = 5
d) string1 = "Rinoceronte"
e) string2 = "Zebra"
f) string3 = "bug”
Para cada uma das seguintes expressões booleanas, classifique-a como
Verdadeira, Falsa ou Ilegal.
● numero1 == numero3 FALSA
● numero1 > numero3 VERDADEIRA
● numero2 < numero3 FALSA
● numero1 == string1 FALSA
● numero1 == "Um" FALSA*
● numero1 == "Trezentos" FALSA*
● numero1 == "300" 
● string2 == "Dois"
● string1 == "Rinoceronte"
● string3 != "Rinoceronte"
● string3 != "Rinoceronte" or numero1 > 1000
● numero2 <= numero1 / 3
● numero1 >= 200
● numero1 >= numero2 + numero3
● numero1 > numero2 and numero1 < numero3
● numero1 == 100 or numero1 > numero3
● numero1 < 10 or numero3 > 10
● numero1 == 30 and numero2 == 100 or numero3 == 100'''

numero1 = 300

if numero1 == "300":
    print("V")
else:
    print("F")
