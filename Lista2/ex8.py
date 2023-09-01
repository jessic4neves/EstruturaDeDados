class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def calcular_media(self):
        if len(self.notas) > 0:
            return sum(self.notas) / len(self.notas)
        else:
            return 0  # Retorna 0 se não houver notas


notas_aluno1 = [8.5, 7.0, 9.2, 6.5]
aluno1 = Aluno("Jessica", notas_aluno1)

notas_aluno2 = [9.0, 8.0, 7.5, 8.5]
aluno2 = Aluno("Thais", notas_aluno2)

media_aluno1 = aluno1.calcular_media()
media_aluno2 = aluno2.calcular_media()

print(f"A média das notas de {aluno1.nome} é {media_aluno1:.2f}")
print(f"A média das notas de {aluno2.nome} é {media_aluno2:.2f}")
