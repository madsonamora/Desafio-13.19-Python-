from Agendamento import Agendamento
def read_from_txt(filename):
    listaAgendamentos = []
    with open(filename, 'r') as file:
        for line in file:
            # Splitting the line into individual variables
            parts = line.strip().split(', ')
            
            # Extracting values from parts
            paciente_id = int(parts[0].split(': ')[1])
            date = parts[1].split(': ')[1]
            time = parts[2].split(': ')[1]
            health_insurance = parts[3].split(': ')[1]
            consultation_type = parts[4].split(': ')[1]

            # Creating a MedicalRecord object and appending it to the list
            record = Agendamento(paciente_id, date, time, health_insurance, consultation_type)
            listaAgendamentos.append(record)

    return listaAgendamentos

if __name__ == "__main__":
    # Reading from the generated text file
    listaAgendamentos = read_from_txt('fake_medical_data.txt')

    # Printing the objects
    for agendamento in listaAgendamentos:
        print(f"Paciente ID: {agendamento.paciente_id}, Date: {agendamento.date}, Time: {agendamento.time}, "
              f"Health Insurance: {agendamento.health_insurance}, Consultation Type: {agendamento.consultation_type}")


