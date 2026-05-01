def equal_split(total_amount, num_people):
    share = total_amount / num_people
    print("\n--- Equal Split ---")
    for i in range(1, num_people + 1):
        print(f"Person {i} pays: {share:.2f}")


def custom_split(total_amount, num_people):
    print("\n--- Custom Split ---")
    contributions = []
    total_entered = 0

    for i in range(1, num_people + 1):
        amount = float(input(f"Enter amount for Person {i}: "))
        contributions.append(amount)
        total_entered += amount

    if abs(total_entered - total_amount) > 0.01:
        print("\n⚠ Warning: Total does not match the bill!")
        print(f"Entered Total: {total_entered}, Actual Bill: {total_amount}")
    else:
        print("\nSplit recorded successfully!")

    print("\n--- Final Contributions ---")
    for i in range(num_people):
        print(f"Person {i+1} pays: {contributions[i]:.2f}")


def main():
    print("====== Budget Splitter ======")

    total_amount = float(input("Enter total bill amount: "))
    num_people = int(input("Enter number of people: "))

    print("\nChoose split method:")
    print("1. Equal Split")
    print("2. Custom Split")

    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        equal_split(total_amount, num_people)
    elif choice == '2':
        custom_split(total_amount, num_people)
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()