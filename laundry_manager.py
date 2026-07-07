#constants for pricing
COST_PER_POUND = 0.5
TAX_RATE = 0.06

#function to print the menu
def print_the_menu():
    # printing menu
    # providing options to the user
    print('\nWhat would you like to do from the following options:\n')
    # the first option
    print('1 --> Calculate total for a customer.')
    # the second option 
    print('2 --> Change price per pound and tax rate.')
    # the third option 
    print('3 --> View customer spending history.')
    # the fourth option
    print('4 --> Quit.')
    
    # asking for the user input from the menu
    selected_option_1 = int(input('\nPlease select the number(1-4) that aligns with your interest from the options: '))
    
    return selected_option_1

#function to print the customer receipt
def print_customer_receipt(user_id,customer_database,tax,total,total_1):
#if the userid is in the dictionary
    if user_id in customer_database:
        customer_database[user_id] += total
        print('\nReceipt:\n')
        print(f'Subtotal: ${total_1:.2f}')
        print(f'Tax:      ${tax:.2f}')
        print('-----------------')
        print(f'Total this time for {user_id}:  ${total:.2f}')
        print(f'Cumulative Total for {user_id}: ${customer_database[user_id]:.2f}')
        
    #if the userid is not in the dictionary     
    else: 
        customer_database[user_id] = total
        print('\nReceipt:\n')
        print(f'Subtotal: ${total_1:.2f}')
        print(f'Tax:      ${tax:.2f}')
        print('-----------------')
        print(f'Total:    ${total:.2f}')


#creating a dictionary to store the data
customer_database = {
    'aryal7931' : 13.0
    
    }

# welcome message
print('Welcome Chief!')

#calling the function to print the menu
selected_option = print_the_menu()

#making sure that the user wants to quit if they choose 4
quit_check = selected_option
while quit_check == 4:
    #asking if the user wants to quit or do they want to view the menu again
    q1 = input("\nAre you sure you want to quit? If yes press any key, if you don't want to quit and want to see the options again press '1': ")
    
    #if the user wants to view the menu again
    if q1 == '1':
        #calling the function to print the menu
        selected_option = print_the_menu()
        quit_check = selected_option
        
    #if the user wants to quit
    else:
        #printing a exit message after user chooses to quit
        print('\nThank you! Have a nice day.')
        quit_check = 0
        
#adding a while loop to run the application until the user selects 4
while selected_option != 4:
    #if statements for the options selection from the menu
    #if user selects 1
    if selected_option == 1:
        #makig sure the user wants to calculate total for a customer
        go_back_1 = input("\nAre you sure you want to calculate total for a customer?\nIf not press '1'\nIf yes press any other key: ")
        #if user wants to calculate total
        while go_back_1 != '1':
            #asking for the userId
            user_id = input('\nEnter your UserId (your last name followed by the last 4 digits of your number): ')
            #asking for the weight of the laundry in pounds
            pounds = float(input('\nEnter the weight of the laundry in pounds: '))
            #calculating the subtotal before tax
            total_1 = pounds * COST_PER_POUND
            #calculating the tax amount
            tax = total_1*TAX_RATE
            #calculating the final total
            total = total_1 + tax
            
            #printing the receipt
            #calling the function to print the receipt
            print_customer_receipt(user_id,customer_database,tax,total,total_1)
                
            #asking the user if they want to keep calculating total(s) for customer(s)
            go_back_1 = input("\nDo you want to keep calculating total(s) for customer(s)? Press any key if yes and press '1' if not: ")
        
    #if user selects 2
    elif selected_option == 2:
        #making sure whether the user wanted to change tax rates or price per pound
        go_back_2 = input("\nAre you sure you want to change tax rates and/or price per pound?\nIf not press '1'\nIf yes press any other key: ")
        #if the user wants to change tax rates and/or price per pound
        while go_back_2 != '1':
            #options for changing tax rates and price per pound
            print('\nHere are your options: \n1 ---> to change the price per pound.\n2 ---> to change the tax rate.\n3 ---> to change both price per pound and tax rate.\n4 ---> Quit.')
            a = int(input('\nPlease select the number(1-4) that aligns with your interest from the options: '))
            
            #if user selects 1
            if a==1:
                COST_PER_POUND = float(input('\nEnter the new price per pound: '))
                #printing updated price per pound
                print(f'Updated price per pound: ${COST_PER_POUND}')
                go_back_2 = input("\nAre you sure about your changes? Press '1' if yes or press any other key if you want to change it again: ")
                
            #if user selects 2
            elif a==2:
                tax_rate_percent = float(input('Enter the new tax rate as percentage (Do not put in percentage sign): '))
                #changing the tax rate to decimal as the user enters it as a percentage
                TAX_RATE = tax_rate_percent / 100
                #printing updated tax rate in decimal
                print(f'Updated tax rate: {TAX_RATE:.2f}')
                go_back_2 = input("\nAre you sure about your changes? Press '1' if yes or press any other key if you want to change it again: ")
                
            #if user selects 3
            elif a==3:
                COST_PER_POUND = float(input('\nEnter the new price per pound: '))
                tax_rate_percent = float(input('Enter the new tax rate as percentage (Do not put in percentage sign): '))
                #changing the tax rate to decimal as the user enters it as a percentage
                TAX_RATE = tax_rate_percent / 100
                #printing updated price per pound
                print(f'Updated price per pound: ${COST_PER_POUND:.2f}')
                #printing updated tax rate in decimal
                print(f'Updated tax rate: {TAX_RATE:.2f}')
                go_back_2 = input("\nAre you sure about your changes? Press '1' if yes or press any other key if you want to change it again: ")
                
            #if user selects 4
            elif a==4:
                go_back_2 = input("\nAre you sure you want to quit? Press '1' if yes or press any other key if you want to continue making changes: ")
            #if user selects anything else
            else:
                #if user selects something other than 1 to 3
                print('\nInvalid entry! Please select from options 1 to 4.')
                go_back_2 = '0'

        
    #if user selects 3
    elif selected_option == 3:
        #making sure the user wanted to view customer spending history
        go_back_3 = input("\nAre you sure you want to view customer spending history?\nIf not press '1'\nIf yes press any other key: ")
        
        #if the user wants to view customer spending history
        while go_back_3 != '1':
            #providing user with options to whether view the spending history of a specific customer or the entire database or quit
            print("\nHere are your options:\n\n1 --> View a specific customer's spending history.\n2 --> View the entire database.\n3 --> Return to the main menu.")
            b = input('\nPlease select the number(1-3) that aligns with your interest from the options: ')
            
            #if the user wants to view the spending history of a certain individual
            if b == '1':
                #asking for the userID
                user_id = input('\nEnter your UserId (your last name followed by the last 4 digits of your number): ')
                #making sure the user entered the correct UserId
                user_check = input(f"Are you sure the UserId is: {user_id}? If yes press any key, if not press '1': ")
                
                #if the user is sure about the USerID
                while user_check != '1':
                #printing the total spent till now by the customer
                    #if the customer is already in the database
                    if user_id in customer_database:
                        print(f'\nThe total spent by {user_id} until now is: ${customer_database[user_id]:.2f}')
                        break
                
                    #if the customer is not in the database
                    else:
                        print('\nInvalid UserId! Not in the database.')
                        break
                    
            #if the user wants to view the entire database
            elif b == '2':
                print("\nAll customers with their total spending till now:\n\nCustomer's UserId:\t\tTotal Spending:")
                print('------------------------------------------------')
                for key,value in customer_database.items():
                    print(f'{key}\t\t\t${value}')
                print('------------------------------------------------')
                
            #if the user wants to quit
            elif b == '3':
                #making sure the user wants to quit or not
                go_back_3 = input('\nAre you sure you want to quit? press 1 if yes, press any other key if you want to continue: ')
            
            #if the user enters anything else other than the options between 1 to 3
            else:
                print('\nInvalid entry! Please select from options 1 to 3.')
                go_back_3 = '0'
    
    #if user selects something other than 1 to 4
    else:
        print('\nInvalid entry! Please select from options 1 to 4.')
    
    #calling the function to print the menu
    selected_option = print_the_menu()
    
    #making sure that the user wants to quit if they choose 4
    quit_check_1 = selected_option
    while quit_check_1 == 4:
        #asking if the user wants to quit or do they want to view the menu again
        q2 = input("\nAre you sure you want to quit? If yes press any key, if you don't want to quit and want to see the options again press '1': ")
        
        #if the user wants to see the options again
        if q2 == '1':
            #calling the function to print the menu
            selected_option = print_the_menu()
            quit_check_1 = selected_option
            
        #if the user wants to quit
        else:
            print('\nThank you! Have a nice day.')
            quit_check_1 = 0
