x = int(input("Digite a quantidade de torcedores do time X:"))

y = int(input("Digite a quantidade de torcedores do time Y:"))

z = int(input("Digite a quantidade de torcedores do time Z:"))

soma = x + y + z

percent_x = 100*x/soma

percent_y = 100*y/soma

percent_z = 100*z/soma

print(f"\nO time X tem {percent_x:.2f}% do total de torcedores;\n\nO time Y tem {percent_y:.2f}% do total de torcedores;\n\nO time Z tem {percent_z:.2f}% do total de torcedores.")