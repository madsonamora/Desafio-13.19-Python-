class Paciente:
    def __init__(self, codigo, nome,convenio,telefone):
        self.codigo = codigo
        self.nome = nome
        self.convenio=convenio
        self.telefone=telefone

    def imprimir(self):
        print(f"{self.nome} ")



    


