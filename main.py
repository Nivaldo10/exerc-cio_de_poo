from cliente import Cliente
from contas import Conta, ContaEspecial
from banco import Banco

joao = Cliente("Joao", "85 984736")
maria = Cliente("Maria da Silva", "85 985465")
conta1 = Conta([joao], 1,100)
conta2 = ContaEspecial([maria, joao],  2, 500, 1000)
conta1.saque(50)
conta2.saque(300)
conta1.saque(190)
conta2.deposito(19.15)
conta2.saque(1500)
conta1.extrato()
conta2.extrato()
tatu = Banco("Tatú")
tatu.abre_conta(conta1)
tatu.abre_conta(conta2)
tatu.lista_contas()