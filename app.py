def calcular_media(nota1, nota2):
    return (nota1 + nota2) /2

print("===Sistema de Notas do Aluno===")
n1 = float(input("digite a primeira Nota:"))
n2 = float(input("Digite a segunda Nota:"))

media = calcular_media(n1, n2)

print(f"A media final è: {media:.2f}")

if media >=7.0:
    print("Status: Aprovado!")
else:
    print("status: reprovado.")