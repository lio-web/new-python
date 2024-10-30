# lib/cli.py
# from seed import reset_database

from helpers import (
    exit_program,
    list_restaurants,
    find_restaurant_by_name,
    find_restaurant_by_id,
    create_restaurant,
    update_restaurant,
    delete_restaurant,
    list_customers,
    find_customer_by_name,
    find_customer_by_id,
    create_customer,
    update_customer,
    delete_customer,
    list_reviews,
    find_review_by_id,
    create_review,
    update_review,
    delete_review
)

def main():
    # reset_database()  # Reset and seed the database at the start
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_restaurants()
        elif choice == "2":
            find_restaurant_by_name()
        elif choice == "3":
            find_restaurant_by_id()
        elif choice == "4":
            create_restaurant()
        elif choice == "5":
            update_restaurant()
        elif choice == "6":
            delete_restaurant()
        elif choice == "7":
            list_customers()
        elif choice == "8":
            find_customer_by_name()
        elif choice == "9":
            find_customer_by_id()
        elif choice == "10":
            create_customer()
        elif choice == "11":
            update_customer()
        elif choice == "12":
            delete_customer()
        elif choice == "13":
            list_reviews()
        elif choice == "14":
            find_review_by_id()
        elif choice == "15":
            create_review()
        elif choice == "16":
            update_review()
        elif choice == "17":
            delete_review()
        else:
            print("Invalid choice")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all restaurants")
    print("2. Find restaurant by name")
    print("3. Find restaurant by ID")
    print("4. Create restaurant")
    print("5. Update restaurant")
    print("6. Delete restaurant")
    print("7. List all customers")
    print("8. Find customer by name")
    print("9. Find customer by ID")
    print("10. Create customer")
    print("11. Update customer")
    print("12. Delete customer")
    print("13. List all reviews")
    print("14. Find review by ID")
    print("15. Create review")
    print("16. Update review")
    print("17. Delete review")

if __name__ == "__main__":
    main()
