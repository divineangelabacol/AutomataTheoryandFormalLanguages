class MealyMachine:
    def __init__(self):
        # Start in state S0
        self.state = "S0"

    def transition(self, bit):
        # Define transitions and outputs based on Mealy Machine logic
        if self.state == "S0":
            if bit == '0':
                self.state = "S1"
                return ""  # No output yet
            elif bit == '1':
                self.state = "S0"
                return ""

        elif self.state == "S1":
            if bit == '1':
                self.state = "S0"
                return "a"  # Output when 01 occurs
            elif bit == '0':
                self.state = "S1"
                return ""

        return ""

    def process(self, binary_string):
        output = ""
        for bit in binary_string:
            if bit not in ('0', '1'):
                raise ValueError("Invalid input: only binary digits (0 or 1) allowed.")
            output += self.transition(bit)
        return output


class MealyApp:
    def __init__(self):
        print("=== Mealy Machine: Detect '01' Sequence ===")
        print("Type 'exit' anytime to quit.\n")

    def run(self):
        while True:
            binary_input = input("Enter a binary string: ").strip()

            # Exit option
            if binary_input.lower() == "exit":
                print("Exiting the program. Goodbye!")
                break

            # Validate input
            if not all(bit in "01" for bit in binary_input):
                print("Invalid input! Please enter only 0s and 1s.")
                continue

            machine = MealyMachine()
            result = machine.process(binary_input)

            if result:
                print(f"Output: {result}")
            else:
                print("No '01' sequence found.")

            # Option for new
            choice = input("Do you want to check another string? (y/n/exit): ").strip().lower()
            if choice in ["n", "exit"]:
                print("Bye Bossing!")
                break


if __name__ == "__main__":
    app = MealyApp()
    app.run()
