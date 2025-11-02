# Hospital Patient Record Management System
# By: Nikita Saharan

class Patient:
    def __init__(self, pid, name, problem):
        self.pid = pid
        self.name = name
        self.problem = problem
        self.next = None

class Hospital:
    def __init__(self):
        self.head = None
        self.undo = []
        self.emergency = []

    # Add patient using linked list
    def add_patient(self, pid, name, problem):
        new_patient = Patient(pid, name, problem)
        new_patient.next = self.head
        self.head = new_patient
        self.undo.append(("add", pid))
        print(f"Patient {name} added.")

    # Delete patient record
    def delete_patient(self, pid):
        temp = self.head
        prev = None
        while temp and temp.pid != pid:
            prev = temp
            temp = temp.next
        if not temp:
            print("Patient not found.")
            return
        if prev:
            prev.next = temp.next
        else:
            self.head = temp.next
        self.undo.append(("del", temp))
        print(f"Patient {temp.name} deleted.")

    # Retrieve patient record
    def get_patient(self, pid):
        temp = self.head
        while temp:
            if temp.pid == pid:
                print(f"ID: {temp.pid}, Name: {temp.name}, Problem: {temp.problem}")
                return
            temp = temp.next
        print("Patient not found.")

    # Undo last action using stack
    def undo_action(self):
        if not self.undo:
            print("No recent action to undo.")
            return
        action, data = self.undo.pop()
        if action == "add":
            self.delete_patient(data)
        elif action == "del":
            self.add_patient(data.pid, data.name, data.problem)

    # Add emergency patient to queue
    def add_emergency(self, name):
        self.emergency.append(name)
        print(f"Emergency patient {name} added to queue.")

    # Handle emergency patient
    def handle_emergency(self):
        if not self.emergency:
            print("No emergency patients.")
        else:
            name = self.emergency.pop(0)
            print(f"Emergency patient {name} is being treated.")

# Polynomial billing example (simple addition)
def calculate_bill(a, b):
    total = a + b
    print("Total Bill:", total)

# Postfix expression evaluation example
def evaluate_postfix(exp):
    stack = []
    for token in exp:
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)
    return stack.pop()

# Main Program
if __name__ == "__main__":
    h = Hospital()
    h.add_patient(1, "Nikita", "Mild Fever")
    h.add_patient(2, "Kartikeya", "Cough and Cold")

    print("\n--- Patient Records ---")
    h.get_patient(1)
    h.get_patient(2)

    print("\n--- Emergency Queue ---")
    h.add_emergency("Nikita")
    h.handle_emergency()

    print("\n--- Inventory Calculation ---")
    result = evaluate_postfix(["2", "3", "+", "4", "*"])
    print("Inventory Result:", result)

    print("\n--- Billing ---")
    calculate_bill(2000, 1500)
