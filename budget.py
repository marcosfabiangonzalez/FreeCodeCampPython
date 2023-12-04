class Category():
    name: str
    ledger: []
    balance: float
    
    def __init__(self, category) -> None:
        self.name = category
        self.ledger = []
        self.balance = 0
        
    def __str__(self) -> str:
        return self.create_expenses_report()

    def deposit(self, amount: float, description: str = "") -> None:
        self.ledger.append({ "amount": amount, "description": description })
        self.get_balance()

    def withdraw(self, amount: float, description: str = "") -> bool:
        if not self.check_funds(amount):
            return False
    
        self.ledger.append({ "amount": -amount, "description": description })
        self.get_balance()
        return True

    def get_balance(self) -> float:
        if len(self.ledger) > 0:
            self.balance = sum(item['amount'] for item in self.ledger)
            
        return self.balance
            
    def transfer(self, amount: float, destination: object) -> bool:
        available = self.withdraw(amount, f"Transfer to {destination.name}")
        
        if available:
            destination.deposit(amount, f"Transfer from {self.name}")
        
        return available
    
    def check_funds(self, amount: float) -> bool:
        return True if amount <= self.balance else False
    
    def create_expenses_report(self) -> str:
        result = self.name.center(30, "*") + "\n" \
                + ''.join(map(self.set_item_to_display, self.ledger)) \
                + f"Total: {self.balance}"
                
        return result
    
    def set_item_to_display(self, item: object) -> str:
        amount = "{0:.2f}".format(item['amount']).strip()
        desc = item['description']
        
        total_chars = 30 - (len(amount) + len(desc))
        
        if total_chars > 0:
            return desc + " " * total_chars + amount + "\n"
        else:
            return f"{desc[:(len(desc)-1+total_chars)]} {amount}\n"

def get_total_withdrawals(categories) -> str:
    axis_x = list(map(lambda r: {"p": r, "value":f"{str(r).rjust(3, ' ')}|"}, range(100, -1, -10)))
    header = ""
    
    for cat in categories:
        total_spent = sum(map(lambda w: w['amount'], [item for item in cat.ledger if item['amount'] < 0]))
        initial_balance = next(map(lambda w: w['amount'], [item for item in cat.ledger if item['amount'] > 0]), None)
        percentage_spent = round(((abs(total_spent)) / initial_balance) * 100, -1)
        
        count = percentage_spent
        for a in axis_x:
            percentage = a['p']
            value = a['value']
            if percentage > count:
                a['value'] += "   "
                continue
            elif count == percentage:
                value += " o "
            else:
                value += "   "
            
            count -= 10 if count > 0 else 0
            a['value'] = value
    
    #header = ''.join(map(lambda r: f"{str(r).rjust(3, ' ')}|\n", range(100, -1, -10)))
    header = ''.join(map(lambda t: t['value'] + "\n", axis_x))
    
    return header

def create_spend_chart(categories) -> str:
    header = get_total_withdrawals(categories)
    footer = " " * 4 + "----------\n"
    lst_names = list(map(lambda i:[*i.name], categories))
    max_name = max(map(len, lst_names))
    
    for inx in range(max_name):
        if inx > 0:
            footer += "\n"
            
        count = 0
        for cat in lst_names:
            if count == 0:
                footer += " " * 5
            if inx < len(cat):
                footer += f"{cat[inx]}  "
            else:
                footer += " " * 3
            count += 1
        
    return f"Percentage spent by category\n{header}{footer}"
                
