# Código da Classe
class Conta:
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo= self.saldo + valor # Ou self.saldo += valor

    def sacar(self, valor):
        if self.saldo < valor:
            return False# Não tem saldo sufíciente
        else:
            self.saldo -= valor
            return True # Saque realizado com sucesso

    def gerar_extrato(self):
        print(f"numero: {self.numero}\ncpf: {self.cpf}\nnome: {self.nomeTitular}\nsaldo: R${self.saldo} ")

    def transfereValor(self, contaDestino, valor):
        if self.saldo < valor:
            return ("Não existe saldo suficiente")
        else:
            contaDestino.depositar(valor)
            self.saldo -= valor
            return ("Transferêcia Realizada!")

# Código do Exemplo
c1 = Conta(1, 12344321, "Ramon", 9000)
c1.depositar(500)

valor_saque = 300
resultado_saque = c1.sacar(valor_saque)

if resultado_saque:
    print(f"Saque de R${valor_saque} realizado com sucesso!")
else:
    print(f"Saldo insuficiente para realizar o saque")

c1.gerar_extrato()

# Código Exemplo 2
conta1 = Conta(123, 88888888, "Maria", 0)
conta2 = Conta(124, 99999999, "Pedro", 500)

print(conta2.transfereValor(conta1, 300))

conta1.gerar_extrato()
conta2.gerar_extrato()

#if conta1 == conta2:
 #   print("São íguais")
#else:
 #   print("São diferentes")