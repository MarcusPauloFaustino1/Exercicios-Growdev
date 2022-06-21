'''3) Crie uma classe para implementar uma conta corrente. A classe
deve possuir os seguintes atributos:
a) número da conta
b) nome do correntista
c) saldo
Os métodos são os seguintes:
a) alterar_nome
b) deposito
c) saque
No construtor, o saldo é opcional, com valor padrão zero e os
demais atributos são obrigatórios.'''

class Account:
    
    def __init__(self, number, name, balance=0):
        self.number = number
        self.name = name
        self.balance = balance
        
    def change_name(self, name):
        self.name = name
        
    def deposit(self, deposit):
        self.balance += deposit
        return self.balance

    
    def withdraw(self, withdraw):
        
        if withdraw > self.balance:
            overdraft = input('Saldo insuficiente ─> Deseja utilisar cheque especial?[s /n]: ')
            if overdraft in 's':
                self.balance -= withdraw
            else:
                print('Saldo insuficiente ─> Não é possível realizar a operação.')
                
        else:
            self.balance -= withdraw    
        return self.balance
    
    def show_info(self):
        print(f'Número da conta: {self.number}\nCorrentista: {self.name}\nSaldo: R$ {self.balance:,.2f}')