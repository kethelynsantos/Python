import random
from pessoa import Pessoa


pessoas = [
    Pessoa('Maciel', 'Não', 'Sim', 'Não', 'Sim', 'Sim', 'Não', 'Não', 'Sim', 'Não', 'Não'),
    Pessoa('Santana', 'Sim', 'Não', 'Não', 'Não', 'Não', 'Não', 'Não', 'Sim', 'Não', 'Não'),
    Pessoa('Byanka', 'Sim', 'Não', 'Sim', 'Sim', 'Não', 'Sim', 'Não', 'Não', 'Não', 'Sim'),
    Pessoa('Kethelyn', 'Sim', 'Não', 'Sim', 'Não', 'Não', 'Não', 'Não', 'Sim', 'Não', 'Não'),
    Pessoa('Felipe', 'Sim', 'Não', 'Não', 'Não', 'Não', 'Sim', 'Sim', 'Não', 'Sim', 'Não'),
    Pessoa('VTorres', 'Sim', 'Sim', 'Sim', 'Não', 'Sim', 'Não', 'Não', 'Não', 'Não', 'Sim'),
    Pessoa('Aprigio', 'Não', 'Não', 'Sim', 'Não', 'Sim', 'Não', 'Não', 'Não', 'Não', 'Não'),
    Pessoa('Beck', 'Não', 'Não', 'Sim', 'Não', 'Não', 'Não', 'Não', 'Não', 'Não', 'Sim'),
    Pessoa('Manuela', 'Sim', 'Não', 'Não', 'Não', 'Não', 'Sim', 'Não', 'Sim', 'Não', 'Sim'),
    Pessoa('Keven', 'Sim', 'Sim', 'Sim', 'Não', 'Não', 'Não', 'Sim', 'Não', 'Sim', 'Sim'),
    Pessoa('Pedrinho', 'Não', 'Não', 'Não', 'Não', 'Não', 'Não', 'Sim', 'Não', 'Sim', 'Não'),
    Pessoa('Prates', 'Sim', 'Não', 'Não', 'Sim', 'Não', 'Não', 'Sim', 'Não', 'Sim', 'Não'),
    Pessoa('Fabio', 'Sim', 'Não', 'Sim', 'Não', 'Não', 'Sim', 'Não', 'Não', 'Não', 'Não'),
    Pessoa('Corsi', 'Não', 'Não', 'Sim', 'Não', 'Não', 'Sim', 'Sim', 'Não', 'Sim', 'Não'),
    Pessoa('Jão', 'Não', 'Não', 'Sim', 'Não', 'Sim', 'Sim', 'Não', 'Não', 'Sim', 'Sim'),
    Pessoa('Rafaela', 'Sim', 'Não', 'Não', 'Não', 'Sim', 'Sim', 'Não', 'Não', 'Sim', 'Sim'),
    Pessoa('Vinicius', 'Não', 'Não', 'Não', 'Não', 'Sim', 'Sim', 'Não', 'Não', 'Não', 'Sim')
]


class QuemSouEu:  # gerencia o jogo
    @staticmethod
    def cabecalho():  # cabecalho
        print("\033[97m*", "\033[97m-" * 22, "\033[97m*")
        print("\033[97m|\033[0m\033[95m      QUEM SOU EU?     \033[0m \033[97m|\033[0m")
        print("\033[97m*", "\033[97m-" * 22, "\033[97m*", "\n")
        print('Bem vindo ao jogo \033[95mQUEM SOU EU\033[0m!'
              '\nVocê tem direito a fazer \033[94m5 perguntas\033[0m '
              'e no final terá \033[94m5 tentativas\033[0m para acertar quem você é.\n')

    def __init__(self, pessoa):  # atributos
        self.pessoa_secreta = None
        self.pessoas = pessoa
        self.dicas = []
        self.vidas = 5

    @staticmethod
    def fazer_pergunta(pessoa, pergunta):
        resposta = getattr(pessoa, pergunta)  # pega o atributo retorna resposta
        return resposta

    def tentativas(self):
        tentativas = 5

        print('\n\033[93m\nVocê pode ser:\033[0m\n')
        for participantes in pessoas:
            print(participantes.nome)

        while True:
            palpite = input(f'\n\033[97mQuem é você?\033[0m Você tem \033[94m{tentativas} tentativas\033[0m: ')
            if palpite.isalpha():
                if palpite.lower() == self.pessoa_secreta.nome.lower():
                    print('\n\033[95mParabéns! Você acertou quem você é.')
                    break
                else:
                    tentativas -= 1
                    if tentativas == 0:
                        print(f'\n\033[91mGAME OVER\033[0m\nVocê era \033[93m{self.pessoa_secreta.nome}.')
                        break
                    else:
                        print(f'\n\033[91mVocê errou!\033[0m')
            else:
                print('\n\033[91mOpção inválida!\033[0m')

    def jogar(self):
        self.pessoa_secreta = random.choice(self.pessoas)

        perguntas = [
            ('\033[97mEu tenho cabelo cacheado?', 'cabelo'),
            ('\033[97mEu sei cantar?', 'musica'),
            ('\033[97mEu sou alto?', 'altura'),
            ('\033[97mEu tenho alguma tatuagem?', 'tatu'),
            ('\033[97mEu namoro?', 'civil'),
            ('\033[97mEu uso óculos?', 'oculos'),
            ('\033[97mEu tenho menos de 18 anos?', 'idade'),
            ('\033[97mEu gosto de front?', 'prefer'),
            ('\033[97mEu curso ensino médio?', 'ensino'),
            ('\033[97mEu já faltei no senai?', 'falta')
        ]

        respostas = []

        for i in range(5):
            print('\033[97m*' + 36 * '\033[96m-\033[0m' + '\033[97m*')
            print('\033[96m|\033[0m          \033[97mEscolha uma opção:\033[0m        \033[96m|\033[0m')
            print('\033[97m*' + 36 * '\033[96m-\033[0m' + '\033[97m*')

            for j, (pergunta, atributo) in enumerate(perguntas):
                print(f'  \033[97m[{j + 1}] | {pergunta}')
                print('\033[97m*' + 36 * '\033[96m-\033[0m' + '\033[97m*')
            escolha = input('\nEscolha uma pergunta: ')

            while not escolha.isnumeric() or int(escolha) < 1 or int(escolha) > 10:
                print('\n\033[91mOpção inválida!\033[0m\n')
                escolha = input('Escolha uma pergunta: ')
            escolha = int(escolha)
            pergunta_escolhida = perguntas[escolha - 1][0]
            atributo = perguntas[escolha - 1][1]
            resposta = self.fazer_pergunta(self.pessoa_secreta, atributo)
            respostas.append((pergunta_escolhida, resposta))

            print(f'\n"{pergunta_escolhida}": {resposta}\n')

        print("\n\033[93mO que você sabe sobre você:")
        for pergunta, resposta in respostas:
            print(f"\033[94m{pergunta}\033[0m {resposta}")

        self.tentativas()

        novamente = input('\n\033[97mDeseja jogar novamente? S/N ')
        if novamente.isalpha():
            if novamente.upper() == 'S':
                self.jogar()
            else:
                print('\n\033[95mBye bye... Obrigado por jogar!\033[0m')
        else:
            print('\n\033[91mOpção inválida!\033[0m')


jogo = QuemSouEu(pessoas)
jogo.cabecalho()
jogo.jogar()
