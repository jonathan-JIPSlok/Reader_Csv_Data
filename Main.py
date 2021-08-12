from Module.Reader_Csv import *

Local_Arquivo = "Casos-e-Obitos-Gov_Sp/Casos_E_Obitos-SP.csv"

Encerrar = False
Tot_Linhas = -1
Data_Search = "all"
while Encerrar == False:
    print("-"*70)
    print("\t\t\t Leitor de dados csv")
    print("-"*70)
    
    print(f"[1] Para usar o arquivo '{Local_Arquivo}'")
    print("[2] Para usar outro arquivo")
    print("\n\t\tDigite 'encerrar' para sair")
    user = str(input("\nOque deseja? "))
    if user == "1":
        pass
    elif user == "2":
        Local_Arquivo = str(input("Endereço: "))
    elif user.lower() == "encerrar":
        Encerrar = True
    
    print("\n[press 'Enter'] Para ler o arquivo todo")
    print("[Digite um número] para ler as linha desejadas")
    print("\n\t\tDigite 'encerrar' para sair")
    
    user = str(input("Oque deseja? "))
    if user == "":
        pass
    elif user.isnumeric() == True:
        Tot_Linhas = int(user)
    elif user.lower() == "encerrar":
        Encerrar = True
    
    print("\n[1] Para pegar todos os dados")
    print("[2] Para pegar dados especificos")
    print("\t\t\t 'encerrar' para sair")
    user = str(input("Oque deseja? "))
    
    if user.lower() == "encerrar":
         Encerrar = True
    elif user.isnumeric() == True:
         if int(user) == 1:
             pass
         elif int(user) == 2:
             Data_Search = str(input("Qual dado deseja? "))
             
    user = str(input("\n[1] Processar dados\n[2] cancelar\nOque deseja? "))
    if user.isnumeric() == True:
        if int(user) == 1:
            print("começando")
            Data = Data_Separator(Local_Arquivo).Reader_Data_Separator(Tot_Linhas)
            if Data_Search == "":
                Data_Search = "all"
            Data_Separator.Print_Detalhing(Data, Data_Search.upper())
            print("fim")
        elif int(user) == 2:
            pass
        elif user.lower() == "encerrar":
            Encerrar = True
        else:
            print("Não entendi! Vamos recomeçar...")