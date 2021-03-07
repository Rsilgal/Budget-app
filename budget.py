class Category:

    def __init__(self, name):
        self.total = 0.0
        self.name = name#.lower()
        self.ledger = []
        # self.ledger = []

    def __str__(self):
        cadena = '{:*^30s}\n'.format(self.name)
        for elem in self.ledger:
            cadena += '{d: <23.23}{a:>7.2f}\n'.format(d= elem['description'], a = elem['amount'])
        cadena += 'Total: {:.2f}'.format(self.total)

        return cadena

    def deposit(self, amount, description = ''):
        if type(amount) is float or int:
            self.total += amount
            self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description = ''):
        if type(amount) is float or int:
            if not self.check_funds(amount):
                return False
            else:    
                self.total -= amount
                self.ledger.append({"amount": -amount, "description": description})
                return True

        return False

    def get_balance(self):
        return self.total

    def transfer(self, amount, category):
        if (type(amount) is float or int) and (type(category) is Category):
            if self.withdraw(amount, 'Transfer to {to}'.format(to = category.name)):
                category.deposit(amount, 'Transfer from {fr}'.format(fr = self.name))
                return True
            return False
        else:
            return False

    def check_funds(self, amount):
        if type(amount) is float or int:
            return self.total >= amount
        else:
            return False

    def percentage_spent(self, total_amount):
        neg_amount = 1

        for elem in self.ledger:
            if elem['amount'] < 0:
                neg_amount += -elem['amount']
        # print((neg_amount / pos_amount) * 100)
        return (neg_amount / total_amount) * 100

def calculate_total_amung(categories):
    total_amoung = 0

    for elem in categories:
        for e in elem.ledger:
            if e['amount'] < 0:
                total_amoung += e['amount']

    return -total_amoung

def create_spend_chart(categories):
    percentage = 100
    cadena = 'Percentage spent by category\n'
    total_amoung = calculate_total_amung(categories)

    for i in range(0,11):
        cadena += '{pcg:>3}| '.format(pcg = percentage)
        for categorie in categories:
            if categorie.percentage_spent(total_amoung) >= percentage:
                cadena += 'o  '
            else:
                cadena += '   '
        
        cadena += '\n'
        percentage -= 10
    
    cadena += '{: <4}'.format('')
    x = ((len(categories) * 3) + 1)
    cadena += '{:-<{}}'.format('', x)

    for categor in categories:
        if categor.name == len(categories[0].name):
            x = len(categor.name)
        elif x < len(categor.name):
            x = len(categor.name)

    for j in range(0,x):
        cadena += '\n{: <5}'.format('')
        for cat in categories:
            if j < len(cat.name):
                cadena += '{}  '.format(cat.name[j])
            else:
                cadena += '   '

    return cadena

