from faker import Faker
import random

fake = Faker()

def generate_fake_medical_data():
    fake_medical_data = []
    for _ in range(100):
        data = {
            'PacienteID': fake.random_int(min=1000, max=9999),
            'Date': fake.date_between(start_date='-30d', end_date='today').strftime('%m/%d/%y'),
            'Time': fake.time(pattern='%H:%M'),
            'HealthInsurance': fake.company(),
            'MedicalConsultationType': random.choice(['NORMAL', 'URGENT', 'SPECIALIST'])
        }
        fake_medical_data.append(data)
    return fake_medical_data

def write_to_txt(fake_medical_data):
    with open('fake_medical_data.txt', 'w') as file:
        for data in fake_medical_data:
            line = (
                f"Paciente ID: {data['PacienteID']}, Date: {data['Date']}, Time: {data['Time']}, "
                f"Health Insurance: {data['HealthInsurance']}, Medical Consultation Type: {data['MedicalConsultationType']}\n"
            )
            file.write(line)

if __name__ == "__main__":
    generated_medical_data = generate_fake_medical_data()
    write_to_txt(generated_medical_data)
