from Paciente import Paciente  

import csv

class MyObject:
    def __init__(self, attribute1, attribute2, attribute3):
        self.attribute1 = attribute1
        self.attribute2 = attribute2
        self.attribute3 = attribute3


csv_file_path = 'D:\\Dados\\Clientes_Arquivo.csv'


listaPacientes = []

# Read the CSV file and create objects
with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    
    # Skip the header row if it exists
    next(csv_reader)

    for linha in csv_reader:        
        codigo, name, convenio, telefone= linha      
          
        # Create an object with the read values and append it to the list        
        paciente = Paciente(codigo, name, convenio,telefone)
        listaPacientes.append(paciente)




