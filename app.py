from classes import AddressBook


def main():
    address_book = AddressBook('address_book.csv')
    print("Address book initialized. Source is:".format(address_book.fp))
    while True:
        command = input("What you want to do? ADD, SHOW, FIND, EXIT")
        """
        Validate input to check that input in these four: ADD, SHOW, FIND, EXIT
        1. Exit: close the program
        2. Add: add record
        3. Show: display records
        4. Find: find records
        """
        if command == 'ADD':
            """
            Ask user what type he want to add (org, person)
            based on this, ask required fields and check field uniqueness if required.
            After adding record show success message in console
            """
            type_ = input('What type do you want to add? (person, org)')
            data = {}
            if type_ == 'person':
                first_name = input('Enter the first name: ')
                last_name = input('Enter the last name: ')
                email = input('Enter the email: ')
                phone_number = input('Enter the phone number: ')
                address = input('Enter the address: ')
                data = {'first_name': first_name,
                        'last_name': last_name,
                        'email': email,
                        'phone_number': phone_number,
                        'address': address}
            if type_ == 'org':
                name = input('Enter the name: ')
                category = input('Enter the category: ')
                phone_number = input('Enter the phone number: ')
                address = input('Enter the address: ')
                data = {'name': name,
                        'category': category,
                        'phone_number': phone_number,
                        'address': address}
            address_book.add_record(type_, data)

        if command == 'SHOW':
            """
            Ask type of records to show: org, person, all
            print records
            """
            type_ = input('What type of records do you want to see? (org, person, all)')
            address_book.get_records(type_)

        if command == 'FIND':
            """
            Ask for type of records to find: org, person, all
            Ask for string to find any text, at least 5 symbols
            print results
            """
            type_ = 'all'
            term = input('What information do you want to see? (at least 5 symbols)')
            address_book.find_record(type_, term)
        if command == 'EXIT':
            raise KeyboardInterrupt


if __name__ == '__main__':
    try:
        main()
    except Exception as err:
        with open('logs.txt', 'a') as f:
            message = '{}    {}:\n {} \n\n'.format(
                datetime.datetime.now(),
                err.__class__.__name__,
                traceback.format_exc()
            )
            f.write(message)
        print('Error was logged!')
    except ValueError as vr:
        print()
