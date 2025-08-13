def feed_pet():
    # start the program
    while True:
        # check if the pet is hungry
        is_hungry = input("is the pet hungry? (yes/no): ").strip().lower()

        if is_hungry == 'yes':
            # select food type
            food_type = input("select food type: ").strip()

            # prepare food
            print(f"preparing {food_type} for the pet...")

            # Feed the pet
            print("feeding the pet...")

            # check if the pet is satisfied
            is_satisfied = input("is the pet satisfied? (yes/no): ").strip().lower()
            if is_satisfied == 'yes':
               print("the pet satisfied!")
        else:
            print("the pet is still hungry.")
        
        clean_up = input("do you wantto clean up? (yes/no): ").strip().lower()
        if clean_up == 'yes':
            print("cleaning up after the pet...")
        
        again = input("do you want to feed the pet again? (yes/no):").strip().lower()
        if again == 'no':
           print("End")
           break  

# Run the feed_pet function
feed_pet()
