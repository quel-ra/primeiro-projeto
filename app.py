#programa de cálculo de média de notas
#autor: Raquel Moura

#entrada 
nome=input("digite o nome do aluno:")
nota1=float(input("digite a primeira nota:"))
nota2=float(input("digite a segunda nota:"))
#processamento
media=(nota1+nota2)/2
#saída
print(f"\nAluno: {nome}")
print(f"Média: {media:.2f}")

if media>=6:
    print("Situação: aprovado!")
else:
    print("Situação reprovado!")