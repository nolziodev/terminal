import cmd

class MyTerminal(cmd.Cmd):
    intro = "Welcome to MyTerminal! Type help or ? to list commands.\n"
    prompt = "myterm> "

    # Custom command: say hello
    def do_hello(self, arg):
        """Say hello"""
        print(f"Hello, {arg or 'friend'}!")

    # Custom command: add numbers
    def do_add(self, arg):
        """Add two numbers. Usage: add 5 10"""
        try:
            a, b = map(float, arg.split())
            print(f"Result: {a + b}")
        except ValueError:
            print("Usage: add <num1> <num2>")

    # Exit command
    def do_exit(self, arg):
        """Exit the terminal"""
        print("Goodbye!")
        return True  # This exits the command loop

    # Catch-all for unknown commands
    def default(self, line):
        print(f"Unknown command: {line}. Type 'help' for a list.")

if __name__ == '__main__':
    MyTerminal().cmdloop()
