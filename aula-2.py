class HistoricoAcademico():
    def __init__(self, aluno):
      self.nome = aluno
      self.media = 0
      self.resultado = False

    def mediaBimestral(self, nota1, nota2):
      self.media = (nota1 + nota2) / 2
      if(self.media >= 7.00):
        self.resultado = True
      return self.media
  
    def mediaFinal(self, notaFinal):
      print(self.notaFinal)
      self.media = (self.media + self.notaFinal) / 2
      if(self.media >= 5.00):
        self.resultado = True
      return self.media

    def resultadoFinal(self):
      if (self.resultado == True and self.media >= 5.00):
        print("Aluno ", self.nome, " foi aprovado no resultado final")
      else:
        print("Aluno ", self.nome, " foi reprovado")


desempenho = HistoricoAcademico("Gael Bertolazzi")
desempenho.mediaBimestral(9, 4)
desempenho.resultadoFinal()