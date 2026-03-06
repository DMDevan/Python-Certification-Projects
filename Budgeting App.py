class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, descriptor = ""):
        self.ledger.append({"amount": amount, "description": descriptor})
        

    def withdraw(self, amount, descriptor = ""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": descriptor})
            return True
        else:
            return False
    
    def get_balance(self): 
        total = 0 
        for item in self.ledger: 
            total += item["amount"] 
        return total
    
    def transfer(self, amount, other_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {other_category.name}")
            other_category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def check_funds(self, amount):
        return amount <= self.get_balance()
    
    def __str__(self):
        title = self.name.center(30, "*")
        items = ""
        for entry in self.ledger:
            desc = entry["description"][:23]
            amt = f'{entry["amount"]:.2f}'
            items += f"{desc:<23}{amt:>7}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + "\n" + items + total

    
def create_spend_chart(categories):
    title = "Percentage spent by category\n"
    bars = "o"
    money_spent = []
    for category in categories:
        total = 0
        for entry in category.ledger:
            if entry["amount"] < 0:
                total += -entry["amount"]
        money_spent.append(total)
    total_spent = sum(money_spent)

    percent = []
    for spent in money_spent:
        pcnt = int ((spent / total_spent) * 100)
        pcnt = pcnt // 10 * 10
        percent.append(pcnt)

    for axis in range(100, -1, -10):
        line = f"{axis:>3}| "
        for pcng in percent:
            if pcng >= axis:
                line += bars + "  "
            else:
                line += "   "
        title += line + "\n"
    title += "    " + "-" * (len(categories) * 3 + 1) + "\n"
    
    names = []
    for category in categories:
        names.append(category.name)
    max_len = 0
    for name in names:
        if len(name) >= max_len:
            max_len = len(name)

    for i in range(max_len):
        line = "     "
        for name in names:
            if i < len(name):
                line += name[i] + "  "
            else:
                line += "   "
        title += line + "\n"
    return title.rstrip("\n")


