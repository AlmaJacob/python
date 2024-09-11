#pet adoption management system

Pets = []

while True:
    print('''
        1. Add Pet
        2. View Pets
        3. Search Pet
        4. Update Pet Details
        5. Delete Pet
        6. Exit''')
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        owner_name = input("Enter the owner's name: ")
        pet_name = input("Enter the pet's name: ")
        pet_type = input("Enter the pet's type (e.g., dog, cat): ")
        pet_age = int(input("Enter the pet's age: "))
        contact_number = int(input("Enter the contact number: "))
        address = input("Enter the address: ")
        Pets.append([owner_name, pet_name, pet_type, pet_age, contact_number, address])
        print("Pet added successfully.")
    
    elif choice == 2:
        if Pets:
            print('_' * 75)
            print('{:<15}{:<15}{:<15}{:<10}{:<15}{:<20}'.format('OWNER NAME', 'PET NAME', 'PET TYPE', 'AGE', 'CONTACT NO', 'ADDRESS'))
            print('_' * 75)
            for pet in Pets:
                print('{:<15}{:<15}{:<15}{:<10}{:<15}{:<20}'.format(pet[0], pet[1], pet[2], pet[3], pet[4], pet[5]))
        else:
            print("No pet details found.")
    
    elif choice == 3:
        pet_name = input("Enter the pet's name: ")
        for pet in Pets:
            if pet[1] == pet_name:
                print('_' * 75)
                print('{:<15}{:<15}{:<15}{:<10}{:<15}{:<20}'.format('OWNER NAME', 'PET NAME', 'PET TYPE', 'AGE', 'CONTACT NO', 'ADDRESS'))
                print('_' * 75)
                print('{:<15}{:<15}{:<15}{:<10}{:<15}{:<20}'.format(pet[0], pet[1], pet[2], pet[3], pet[4], pet[5]))
                break
        else:
            print("Pet not found.")
    
    elif choice == 4:
        pet_name = input("Enter the pet's name to update: ")
        for pet in Pets:
            if pet[1] == pet_name:
                print("1. Update Owner Name")
                print("2. Update Pet Type")
                print("3. Update Pet Age")
                print("4. Update Contact Number")
                print("5. Update Address")
                update_choice = int(input("What would you like to update? "))
                
                if update_choice == 1:
                    pet[0] = input("Enter new owner's name: ")
                elif update_choice == 2:
                    pet[2] = input("Enter new pet type: ")
                elif update_choice == 3:
                    pet[3] = int(input("Enter new pet age: "))
                elif update_choice == 4:
                    pet[4] = int(input("Enter new contact number: "))
                elif update_choice == 5:
                    pet[5] = input("Enter new address: ")
                print("Pet details updated successfully!")
                break
        else:
            print("Pet not found.")
    
    elif choice == 5:
        pet_name = input("Enter the pet's name to delete: ")
        for pet in Pets:
            if pet[1] == pet_name:
                Pets.remove(pet)
                print("Pet deleted successfully!")
                break
        else:
            print("Pet not found.")
    
    elif choice == 6:
        print("Exiting...")
        break
    
    else:
        print("Invalid choice. Please try again.")
