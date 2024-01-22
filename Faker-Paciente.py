from faker import Faker

fake = Faker()

def generate_fake_data():
    fake_data = []
    for _ in range(100):
        data = {
            'd': fake.date,
            'Name': fake.name(),
            'Cellphone': fake.phone_number(),
            'HealthInsurance': fake.company()
        }
        fake_data.append(data)
    return fake_data

def write_to_txt(fake_data):
    with open('fake_data.txt', 'w') as file:
        for data in fake_data:
            line = f" {data['d']},  {data['Name']},  {data['Cellphone']}, {data['HealthInsurance']}\n"
            file.write(line)

if __name__ == "__main__":
    generated_data = generate_fake_data()
    write_to_txt(generated_data)
