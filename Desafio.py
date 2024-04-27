menu = '''

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> '''

saldo = 0
limite= 500
extrato= ""
numero_saques= 0
LIMITE_SAQUES= 3

while True:
   
   opcao= input(menu)

   if opcao == "1":
     valor = float(input("Informe o valor do depósito: "))
     if valor >= 0:
        saldo +=valor
        extrato += f" Depósito: R$ {valor :.2f}\n"

     else: 
        print("Falha na operação, valor inválido.")
     
   elif opcao == "2":
       valor = float(input("Informe o valor do saque: "))
       excedeu_saldo = valor> saldo
       excedeu_limite = valor> limite
       excedeu_saques = numero_saques>= LIMITE_SAQUES

       if excedeu_saldo:
          print("Falha na operação, saldo insulficiente.")

       elif excedeu_limite:
           print("Falha na operação, valor de saque excede o limite.")
       elif excedeu_saques:
          print(" Falha na operação, número máximode saques excedido.")

       elif valor >0:
          saldo-=valor
          extrato += f"Saque: R$ {valor:.2f}\n"
          numero_saques +=1

       else:
         print("Falha na operação, valor informado é inválido")
   
 
   elif opcao == "3":
      print("\n===================Extrato===================")
      print("Não foram realizadas movimentações." if not extrato else extrato)
      print(f"\nSaldo: R$ {saldo:.2f} ")          
      print("===============================================")  
      
   elif opcao == "0":
      break
      
   else:
      print("Operação inválida, por favor selecione novamente a opção desejada.")