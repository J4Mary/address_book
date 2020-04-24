import csv


class Record:

    def __init__(self, phone_number, address=None):
        self.phone_number = phone_number  # this should be unique
        try:
            self.validate_phone_number()
        except FileNotFoundError:
            print('phone_numbers.txt file was not found. '
                  'No validation provided')
        self.save_phone_number()
        self.address = address

    def save_phone_number(self, phone_number):
        with open('phone_numbers.txt', 'a') as f:
            f.write(self.phone_number)
            f.write('\n')

    def validate_phone_number(self):
        with open('email.txt', 'r') as f:
            phone_numbers = f.read()
        if self.phone_number.lower() in phone_numbers:
            raise ValueError

    def __str__(self):
        raise NotImplementedError

    @classmethod
    def from_csv(cls, fp):
        raise NotImplementedError


class Person(Record):
    def __init__(self, first_name, last_name, email, phone_number, address=None):
        super().__init__(phone_number, address)
        self.first_name = first_name
        self.last_name = last_name
        self.email = email  # this should be unique
        try:
            self.validate_email()
        except FileNotFoundError:
            print('email.txt file was not found. '
                  'No validation provided')
        self.save_email()

    def save_email(self, email):
        with open('emails.txt', 'a') as f:
            f.write(self.email)
            f.write('\n')

    def validate_email(self):
        with open('email.txt', 'r') as f:
            emails = f.read()
        if self.email.lower() in emails:
            raise ValueError

    @classmethod
    def from_csv(cls, fp):
        """
        + Read data from file
        + Compose data from file with properties
        + Generate object
        """
        obj_list = []
        with open(fp, 'r') as fp:
            file_data = [row for row in csv.DictReader(fp)]
        for row in file_data:
            if row['type'] == 'Person':
                first_name = row['first_name']
                last_name = row['last_name']
                email = row['email']
                phone_number = row['phone']
                address = row['address']
                obj_list.append(cls(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    phone_number=phone_number,
                    address=address
                ))
        return obj_list


class Organization(Record):
    def __init__(self, name, category, phone_number, address):
        super().__init__(phone_number, address)
        self.name = name  # this should be unique
        try:
            self.validate_name()
        except FileNotFoundError:
            print('names.txt file was not found. '
                  'No validation provided')
        self.save_name()
        self.category = category

    def save_name(self, name):
        with open('names.txt', 'a') as f:
            f.write(self.name)
            f.write('\n')

    def validate_name(self):
        with open('names.txt', 'r') as f:
            names = f.read()
        if self.name.lower() in names:
            raise ValueError

    @classmethod
    def from_csv(cls, fp):
        """
        + Read data from file
        + Compose data from file with properties
        + Generate object
        """
        obj_list = []
        with open(fp, 'r') as fp:
            file_data = [row for row in csv.DictReader(fp)]
        for row in file_data:
            if row['type'] == 'Organization':
                name = row['name']
                category = row['category']
                phone_number = row['phone']
                address = row['address']
                obj_list.append(cls(
                    name=name,
                    category=category,
                    phone_number=phone_number,
                    address=address
                ))
        return obj_list


class AddressBook:
    def __init__(self, fp):
        self.fp = fp

    def validate_person(self, data):
        pass

    def validate_org(self, data):
        pass

    @staticmethod
    def add_record(self, type_, data):
        with open('address_book.csv', 'w') as a:
            writer = csv.DictWriter(a, delimiter=',', fieldnames=('type', 'phone', 'address', 'name', 'category',
                                                                  'first_name', 'last_name', 'email'))
            if type_ == 'person':
                writer.writerow({'type': 'Person',
                                 'first_name': data['first_name'],
                                 'last_name': data['last_name'],
                                 'email': data['email'],
                                 'phone_number': data['phone_number'],
                                 'address': data['address']})
            if type_ == 'org':
                writer.writerow({'type': 'Organization',
                                 'name': data['name'],
                                 'category': data['category'],
                                 'phone_number': data['phone_number'],
                                 'address': data['address']})

    @staticmethod
    def find_record(self, type_, search_term):
        with open('address_book.csv', 'r') as fp:
            print([row for row in csv.DictReader(fp) if row.find(search_term)[0] != -1])

    @staticmethod
    def get_records(self, type_):
        with open('address_book.csv', 'r') as fp:
            if type_ == 'person':
                print([row for row in csv.DictReader(fp) if row.split(',')[0] == 'Person'])
            if type_ == 'org':
                print([row for row in csv.DictReader(fp) if row.split(',')[0] == 'Organization'])

    @staticmethod
    def import_from_csv(self, fp):
        with open(fp, 'r') as fp:
            file_data = [row for row in csv.DictReader(fp)]
        with open('address_book.csv', 'w') as a:
            writer = csv.DictWriter(a, delimiter=',', fieldnames=('type', 'phone', 'address', 'name', 'category',
                                                                  'first_name', 'last_name', 'email'))
        for row in file_data:
            writer.writerow(row)
