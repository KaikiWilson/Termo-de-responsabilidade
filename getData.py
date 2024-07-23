day = input('Insira o dia de recebimento do equipamento: ')
week = input('Agora insira o mês de recebimento do equipamento: ')
year = input('Por último, insira o ano de recebimento do equipamento: ')

usuariName = str.upper(input('Nome do solicitante: '))
usuariCPF = input('CPF do solicitante: ')
usuariPhoneNumber = input('Número de telefone do solicitante: ')

class usuariData:
    def __init__(self, className, classCPF, classEmail, classPhoneNumber):
        self.name = className
        self.cpf = classCPF
        self.email = classEmail
        self.phoneNumber = classPhoneNumber

requestingUser = usuariData(className=usuariName, classCPF=usuariCPF, classEmail='N/A', classPhoneNumber=usuariPhoneNumber)