class Pessoa:  # define os atributos das pessoas
    def __init__(self, nome, cabelo, musica, altura, tatu, civil, oculos,
                 idade, prefer, ensino, falta):
        self.__nome = nome
        self.cabelo = cabelo
        self.musica = musica
        self.altura = altura
        self.tatu = tatu
        self.civil = civil
        self.oculos = oculos
        self.idade = idade
        self.prefer = prefer
        self.ensino = ensino
        self.falta = falta

    @property
    def nome(self):
        return self.__nome
