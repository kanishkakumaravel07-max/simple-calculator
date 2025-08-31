class Employee:
    def init(self, name, basic, hra, da, tax_rate):
        self.name = name
        self.basic = basic
        self.hra = hra
        self.da = da
        self.tax_rate = tax_rate

    def calculate_net_salary(self):
        gross = self.basic + self.hra + self.da
        tax = (self.tax_rate / 100) * gross
        return gross - tax

    def display_salary(self):
        print(f"\nEmployee Name: {self.name}")
        print(f"Net Salary: {self.calculate_net_salary():.2f}")


def main():
    employee = None

    while True:
        print("\n--- Employee Salary Menu ---")
        print("1. Create Employee")
        print("2. Calculate & Display Net Salary")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            name = input("Enter employee name: ")
            basic = float(input("Enter Basic Salary: "))
            hra = float(input("Enter HRA: "))
            da = float(input("Enter DA: "))
            tax_rate = float(input("Enter Tax Rate (%): "))
            employee = Employee(name, basic, hra, da, tax_rate)
            print("Employee created successfully!")

        elif choice == '2':
            if employee:
                employee.display_salary()
            else:
                print("Please create an employee first.")

        elif choice == '3':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter 1, 2, or 3.")


if name == "main":
    main()
