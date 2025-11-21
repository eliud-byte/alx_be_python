def display_menu():
    print("\n<---------------################------------->")
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("\nEnter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            item = input("\nWhat would you like to add: ")
            shopping_list.append(item)
            print(f"{item} added to shopping list.")

        elif choice == '2':
            # Prompt for and remove an item
            item = input("\nWhat would you like to remove: ")
            if  item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} removed from shopping list.")
            else:
                print(f"{item} is not on your list.")

        elif choice == '3':
            # Display the shopping list
            print("\nYour shopping list items are:")
            for item in shopping_list:
                print(item)

        elif choice == '4':
            print("\nGoodbye!")
            break
        
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()