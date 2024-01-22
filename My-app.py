from Paciente import Paciente
from Agendamento import Agendamento
import csv

def main():
  
    listaPacientes=[]
    listaAgendamentos=[]
    p1= Paciente(2332, nome="madson", convenio="santa casa",telefone="34234-4345")
    p2= Paciente(33, nome="madson amora ferreia", convenio="santa casa",telefone="34234-4345")
    lerArquivo(listaPacientes)
    while True:
        print("\nMenu:")
        print("1. Cadastramento de pacientes.")
        print("2. Agendamento de consultas.")
        print("3. Alteração de pacientes.")
        print("4. Visualização de consultas.")
        print("5. Geração de arquivo auxiliar.")
        print("6. Mostrar Agendamentos")
        print("7. Mostrar Pacientes cadastrados")
        print("0. Sair.")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
        
            cadastroPaciente(listaPacientes)
        
        elif opcao == "2":
           fazerAgendamento("455",listaAgendamentos)
        elif opcao == "3":
            alterar_paciente()
        elif opcao == "4":
            visualizar_consultas()
        elif opcao == "5":
            gerar_arquivo_auxiliar()
        elif opcao == "6":
            mostrarAgendamentos(listaAgendamentos)
        elif opcao == "7":
            gerar_arquivo_auxiliar()
        elif opcao == "0":
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")
   
   
   # fazerAgendamento(p1.codigo,agendamentos)
    listaAgendamentos.append(Agendamento(data="10/23/34", horas="12:23",codigoPaciente=p1.codigo,tipoConsulta="NORMAL"))
   # cadastramentoPacientes(pacientes)    
    
   # for agendamento in listaAgendamentos:
   #     print(agendamento.data)
   #     print(agendamento.codigoPaciente)
  
def mostrarAgendamentos(listaAgendamentos):
    for agendamento in listaAgendamentos:
        print("for")
        print(f"{agendamento.codigoPaciente}{agendamento.data}{agendamento.horas}{agendamento.tipoConsulta}")

def lerArquivoAgendamentos(listaAgendamentos):
    input("digite o nome do cliente")
        
def lerArquivoPacientes(listaPacientes):   
    filePath = "D:\\Dados\\Clientes_Arquivo.csv"
    
    with open(filePath, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for linha in reader:
            codigo,name,convenio,telefone= linha              
            
            paciente=Paciente(codigo,name,convenio,telefone)
            listaPacientes.append(paciente)
        
def buscarPaciente(nome, listaPacientes):   
    for paciente in listaPacientes:
     if(nome==paciente.nome):
        return paciente
    print("paciente nao encontrado!")        
    return None
        
def cadastroPaciente(listaPacientes):   
    id=input("Digite o id")  
    nome=input("digite o nome do paciente")   
    
    convenio=input("digite o nome do convenio")
    telefone=input("digite o telefone")
    
    paciente=Paciente(id,nome,convenio,telefone)    
    listaPacientes.append(paciente)
    
def alterarPaciente(listaPaciente):
    nome=input("Digite o nome do paciente")
    for paciente in listaPaciente:
        if(paciente.nome==nome):
            listaPaciente.remove(paciente)
            print(paciente.nome+" removido")
        else:
            print("paciente nao achado")    
        
def fazerAgendamento(pacienteId,agendamentos):
    
    data=input("Digite a data do agendamento")
    horas=input("Digite as horas")
    tipoConsulta=input("Digite o tipo de consulta")
    agend=Agendamento(data,horas,pacienteId,tipoConsulta)
    agendamentos.append(agend)
        

   



    
if __name__ == "__main__":
    main()     