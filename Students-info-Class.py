"""Crie uma classe representando os alunos de um determinado curso. A classe deve
conter os atributos matricula do aluno, nome, nota da primeira prova, nota da segunda
prova e nota da terceira prova. Crie metodos para acessar o nome e a m  edia do aluno. 
(a) Permita ao usuario entrar com os dados de 5 alunos. 
(b) Encontre o aluno com maior media geral. 
(c) Encontre o aluno com menor media geral 
(d) Para cada aluno"""

class Aluno:
    alunos =[]
    medias = []

    def __init__(self, nome, matricula, np1, np2, np3, media=None):
        self.nome = nome
        self.matricula = matricula
        self.np1 = np1
        self.np2 = np2
        self.np3 = np3
        self.media = media
        Aluno.alunos.append(self)

    def get_nome(self):
        return self.nome
    
    def calcula_media(self):
        soma = self.np1 + self.np2 + self.np3
        self.media = soma // 3
        Aluno.medias.append(self.media)

    def verifica_media(self):
        print(f'O aluno(a) {self.nome} obteve uma média de {self.media}.')

    @classmethod
    def media_alunos(cls):
        for aluno in cls.alunos:
            aluno.calcula_media()
            aluno.verifica_media()

    @classmethod
    def verifica_maior_media(cls):
        maior_media = 0
        aluno_maior_media = None

        for aluno in cls.alunos:
            aluno.calcula_media()

            if aluno.media > maior_media:
                maior_media = aluno.media
                aluno_maior_media = aluno

        aluno_maior_media.verifica_media()

    @classmethod
    def verifica_menor_media(cls):
        menor_media = 10
        aluno_menor_media = None

        for aluno in cls.alunos:
            aluno.calcula_media()

            if aluno.media < menor_media:
                menor_media = aluno.media
                aluno_menor_media = aluno

        aluno_menor_media.verifica_media()

    @classmethod
    def verifica_aprovacao(cls):
        for aluno in cls.alunos:
            aluno.calcula_media()

            if aluno.media >= 6:
                print('O', aluno.get_nome(), 'foi aprovado!')
            else:
                print('O', aluno.get_nome(), 'foi Reprovado.')


aluno1 = Aluno('Ana', 111, 5, 9, 4)
aluno2 = Aluno('Bia', 222, 9, 2, 5)
aluno3 = Aluno('Caio', 333, 2, 10, 7)
aluno4 = Aluno('Duda', 444, 7, 8, 10)
aluno5 = Aluno('Eli', 555, 10, 7, 3)


