import csv

class Data_Separator():
    """
    Created By JIPSlok
    
    Funcões:
        __init__
            Parametro Local_File -> Local do arquivo csv para ser feito a abertura em modo de leitura
        Pegar_Dados
            Parametro Csv_Object -> Objeto csv que contem o arquivo já aberto
            Parametro Linhas -> Número de linhas que ser percorrido, por padrao vem -1 que faz percorrer o arquivo todo
            
            A função retorna uma lista com os dados do arquivo
        
        Reader_File
            Lê o arquivo csv, Retorna um objeto csv
            
        Close_File
            Fecha o arquivo csv
        
        Separator_Lines
            Parametro Lines -> Dados do arquivo csv que foram lidos
            
            Separa os dados do arquivo criando uma lista com cada item
        
        Reader_Data_Separator
            Parametro Lines_Data -> Total de linhas para serem lidas
            
            retorna os dados ja separados por linhas, é uma junção das outras funcões.
            
        Print_Detalhing
            Parametro Data -> Dados do arquivo csv para serem tratados
            Parametro Information -> por padrão vem "all" para pegar todos os dados, esse parametro recebe oque você procura dentro do arquivo
            
            Imprime os dados de acordo com oque você procura que deve ser passado no parametro Information
            
    """
    def __init__(self, Local_File):
        self.Local_File = Local_File 
        self.Arquivo = open(self.Local_File, "r") #Abre o Arquivo csv em modo de leitura
        
    def Pegar_Dados(self, Csv_Object, Linhas = -1):
        Data = []
        Cont = 0
        for data in Csv_Object:
            Data.append(data)
            if Cont == Linhas:
                break
            else: Cont += 1
        return Data
    
    def Reader_File(self): # Le o arquivo csv
        leitor = csv.reader(self.Arquivo)
        return leitor
    
    def Close_File(self): #Fecha o arquivo csv
        self.Arquivo.close()
        
    def Separator_Lines(self, Lista): # Separa os dados do arquivo, criando uma lista como cada item
        List_Data = []
        Line_Data = []
        Palavra = ""
        
        for List in Lista: #percorre todas as listas dentro do arquivo
            for Line in List: #Pega todas as linhas dentro da lista
                for Letra in Line: #Pega todas as Letras dentro da linha
                    if Letra != ";" : #Forma uma palavra com as letras
                        Palavra += Letra
                    elif Letra == ";": #Separa as palavra por ";"
                        Line_Data.append(Palavra)
                        Palavra = ""
                if len(Line_Data) != 0: #Adiciona a linha a lista
                    List_Data.append(Line_Data)
                    Line_Data = []
                    
        return List_Data
    
    def Reader_Data_Separator(self, Lines_Data = -1): #Le os dados, separa por linha
        Data = self.Reader_File() #Le o Arquivo
        Data = self.Pegar_Dados(Data, Lines_Data) #Pega os dados do arquivo
        Data = self.Separator_Lines(Data) #Separa por linhas
        self.Close_File() #fecha o arquivo
        return Data
        
    def Print_Detalhing(Data, Information = "ALL"): #Imprime os dados formatados
        cont = 0
        cont_Item = 0
        for List in Data: #Percorre todas as Listas de Data
            if cont == 0:
                pass
            elif Information == "ALL": #Pega todos os items caso nenhum dado seja informado pelo usuario
                print("-"*70)
                for Item in List:
                    print(f"{Data[0][cont_Item]}:\t\t{Item}")
                    cont_Item += 1
                cont_Item = 0
            else:
                if Information.upper() in List: #Pega apenas os dados que corresponde ao que foi passado pelo usuario
                    print("-"*70)
                    for Item in List:
                        print(f"{Data[0][cont_Item]}:\t\t{Item}")
                        cont_Item += 1
                cont_Item = 0
            cont += 1