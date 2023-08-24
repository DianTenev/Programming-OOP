from project.clients.adult import Adult
from project.clients.student import Student
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    LOAN_TYPES = {'StudentLoan': StudentLoan, 'MortgageLoan': MortgageLoan}
    CLIENT_TYPES = {"Student": Student, "Adult": Adult}

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans = []
        self.clients = []

    def add_loan(self, loan_type: str):
        if loan_type not in self.LOAN_TYPES:
            raise Exception("Invalid loan type!")
        self.loans.append(self.LOAN_TYPES[loan_type]())
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.CLIENT_TYPES:
            raise Exception("Invalid client type!")
        if len(self.clients) >= self.capacity:
            return "Not enough bank capacity."
        self.clients.append(self.CLIENT_TYPES[client_type](client_name, client_id, income))
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        current_client = [x for x in self.clients if x.client_id == client_id][0]
        if current_client.__class__.__name__ == "Student":
            if loan_type != "StudentLoan":
                raise Exception("Inappropriate loan type!")
            current_loan = [x for x in self.loans if x.__class__.__name__ == loan_type][0]
            self.loans.remove(current_loan)
            current_client.loans.append(self.LOAN_TYPES[loan_type]())
            return f"Successfully granted {loan_type} to {current_client.name} with ID {client_id}."

        elif current_client.__class__.__name__ == "Adult":
            if loan_type != "MortgageLoan":
                raise Exception("Inappropriate loan type!")
            current_loan = [x for x in self.loans if x.__class__.__name__ == loan_type][0]
            self.loans.remove(current_loan)
            current_client.loans.append(self.LOAN_TYPES[loan_type]())
            return f"Successfully granted {loan_type} to {current_client.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        clients = [x for x in self.clients if x.client_id == client_id]
        if not clients:
            raise Exception("No such client!")
        if clients[0].loans:
            raise Exception("The client has loans! Removal is impossible!")
        self.clients.remove(clients[0])
        return f"Successfully removed {clients[0].name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        filtered_loans = [loan for loan in self.loans if loan.LOAN_TYPE == loan_type]
        [loan.increase_interest_rate() for loan in filtered_loans]
        return f"Successfully changed {len(filtered_loans)} loans."

    def increase_clients_interest(self, min_rate: float):
        counter = 0
        for client in self.clients:
            if client.interest < min_rate:
                client.increase_clients_interest()
                counter += 1
        return f"Number of clients affected: {counter}."

    def get_statistics(self):
        total_income = 0
        granted_loans = 0
        granted_sum = 0
        for i in self.clients:
            total_income += i.income
            for j in i.loans:
                granted_loans += 1
                granted_sum += j.amount

        non_granted_loans_sum = 0
        for i in self.loans:
            non_granted_loans_sum += i.amount

        interest_rate = 0
        for i in self.clients:
            interest_rate += i.interest
        if len(self.clients) != 0:
            interest_rate /= len(self.clients)

        return f"Active Clients: {len(self.clients)}\n" \
               f"Total Income: {total_income:.2f}\n" \
               f"Granted Loans: {granted_loans}, Total Sum: {granted_sum:.2f}\n" \
               f"Available Loans: {len(self.loans)}, Total Sum: {non_granted_loans_sum:.2f}\n" \
               f"Average Client Interest Rate: {interest_rate:.2f}"


bank = BankApp(3)

print(bank.add_loan('StudentLoan'))
print(bank.add_loan('MortgageLoan'))
print(bank.add_loan('StudentLoan'))
print(bank.add_loan('MortgageLoan'))


print(bank.add_client('Student', 'Peter Simmons', '1234567891', 500))
print(bank.add_client('Adult', 'Samantha Peters', '1234567000', 1000))
print(bank.add_client('Student', 'Simon Mann', '1234567999', 700))
print(bank.add_client('Student', 'Tammy Smith', '1234567555', 700))

# print(bank.grant_loan('StudentLoan', '1234567891'))
print(bank.grant_loan('MortgageLoan', '1234567000'))
# print(bank.grant_loan('MortgageLoan', '1234567000'))

print(bank.remove_client('1234567999'))

print(bank.increase_loan_interest('StudentLoan'))
print(bank.increase_loan_interest('MortgageLoan'))

print(bank.increase_clients_interest(1.2))
print(bank.increase_clients_interest(3.5))

print(bank.get_statistics())

