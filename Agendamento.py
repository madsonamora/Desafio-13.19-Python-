#data, hora, código do paciente, tipo consulta — Normal ou Retorno)

class Agendamento:
    def __init__(self, data, horas,codigoPaciente,tipoConsulta):
        self.data = data
        self.horas = horas
        self.codigoPaciente=codigoPaciente
        self.tipoConsulta=tipoConsulta

    def imprimir(self):
        print(f"{self.codigoPaciente} ")
