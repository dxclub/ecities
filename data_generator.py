import names, randominfo, csv, random

# DATA_GENERATOR - Created by Luis Plascencia
#
# This code was used to create the ecities.csv file. This program generates random names, emails, passwords and phone numbers
# that are written row by row into a csv. The four main columns are NAMES, EMAIL ADDRESS, PASSWORDS, and PHONE NUMBERS.
# 
# The overall goal of the challenge was to create thousands of different names in order to hide one person of interest between 
# the thousands of people listed, in this ecities challenge, I used Julius Caesar as the person of interest due to
# the infamous Caesar Shift Cipher that is popularly known in the cybersecurity world. Hence the picture of Rome in this repo!
#
# Once you run this code, enter the number of people you want to generate, whether to randomize or not, and enjoy the creation!

emails = ["@paris.com", "@newyork.com", "@london.com", "@dubai.com", "@hongkong.com", "@singapore.com", 
          "@rome.com", "@beijing.com", "@tokyo.com", "@moscow.com", "@barcelona.com", "@istanbul.com"]

def main():
    while(True):
        count = input("Enter the number of random people you want to create: ")
        if not count.isnumeric():
            print("Please enter an integer!")
        else:
            count = int(count)
            break

    new_decision = input("Are you sure you want to create a new CSV file (Y/N)? ")
    randomize = input("Do you want to randomize the data (Y/N)? ")
    if new_decision.lower() == "y":
        people_list = people_gen(count)
        with open('test.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["NAMES", "EMAIL ADDRESS", "PASSWORDS", "PHONE NUMBERS"])
            if randomize.lower() == "y":
                for person in people_list:
                    details = [person.name, person.email, person.password, person.phone_number]
                    rando = random.sample(details, 4)
                    writer.writerow(rando)
            else:
                for person in people_list:
                    writer.writerow([person.name, person.email, person.password, person.phone_number])
        print("Done")
    
class People:
    def __init__(self):
        self.name = names.get_full_name()
        self.email = self.name.replace(" ", "").lower() + emails[random.randint(0, 11)]
        self.password = randominfo.random_password(8, special_chars=False, digits=True)
        self.phone_number = f"{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}"

    def __repr__(self):
        return (f"Name: {self.name}, Email: {self.email}, "
                f"Password: {self.password}, Phone Number: {self.phone_number}")

def people_gen(count):
    people_list = []
    for i in range(count):
        person = People()
        print(f"Count: {i+1}", end = '\r')
        people_list.append(person)
    print("\r")
    return people_list

if __name__ == '__main__':
    main()