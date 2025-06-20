import random

class Context:
    def __init__(self):
        self.simple_options = {}

    def __getattr__(self, item):
        if item in self.simple_options:
            return self.simple_options[item]
        raise AttributeError(f"'Context' object has no attribute '{item}'")

class CommonCommandProcessor:
    def __init__(self):
        self.ctx = Context()
        self.output_calls = [] # Para registrar as chamadas de output
        self.marker = ""

    def output(self, message):
        self.output_calls.append(message)

    def _cmd_options(self):
        """List all current options. Warning: lists password."""
        self.output("Current options:")
        for option in self.ctx.simple_options:
            if option == "server_password" and self.marker == "!":  # Decision 1
                self.output(f"Option server_password is set to " + ("*" * random.randint(4, 16)))
            else:
                self.output(f"Option {option} is set to {getattr(self.ctx, option)}")

# --- Casos de Teste MC/DC ---

# CT1: option é "server_password" e self.marker é "!"
def run_ct1():
    processor = CommonCommandProcessor()
    processor.marker = "!"
    processor.ctx.simple_options = {
        "server_password": "mysecretpassword",
        "other_option": "value_other"
    }
    # Mock random.randint para consistência
    original_randint = random.randint
    random.randint = lambda a, b: 8

    processor._cmd_options()
    print("\n--- CT1 Output ---")
    for call in processor.output_calls:
        print(call)
    print("Expected: Option server_password is set to ********")
    print("Expected: Option other_option is set to value_other")

    random.randint = original_randint # Restaurar random.randint

# CT2: option NÃO é "server_password" e self.marker é "!"
def run_ct2():
    processor = CommonCommandProcessor()
    processor.marker = "!"
    processor.ctx.simple_options = {
        "other_option": "value_other",
        "another_option": "another_value"
    }
    processor._cmd_options()
    print("\n--- CT2 Output ---")
    for call in processor.output_calls:
        print(call)
    print("Expected: Option other_option is set to value_other")
    print("Expected: Option another_option is set to another_value")

# CT3: option é "server_password" e self.marker NÃO é "!"
def run_ct3():
    processor = CommonCommandProcessor()
    processor.marker = "#"
    processor.ctx.simple_options = {
        "server_password": "mysecretpassword",
        "other_option": "value_other"
    }
    processor._cmd_options()
    print("\n--- CT3 Output ---")
    for call in processor.output_calls:
        print(call)
    print("Expected: Option server_password is set to mysecretpassword")
    print("Expected: Option other_option is set to value_other")

if __name__ == "__main__":
    run_ct1()
    run_ct2()
    run_ct3()