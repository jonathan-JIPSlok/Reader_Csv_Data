import csv

class Data_Writer():
    """
           Created By Jonathan-JIPSlok
            
           Objetivo: Escrever em arquivos .csv
    """
    def __init__(self):
        """
            File -> deve receber o local do arquivo e o nome.csv
            Open_Mode -> Modo de leitura, por padrao vem W (para criar um arquivo zerado)
            newline -> Como o csv deve tratar os finais de linhas ("", "\n")
        """
        self.File = ""
        self.Open_Mode = "w"
        self.newline = ""
       
    def Open_File(self): #Abre ou cria o arquivo csv
        self.File_Opened = open(self.File, self.Open_Mode, newline = self.newline)
        
    def Close_File(self): # Fecha o arquivo csv oque é essencial
        self.File_Opened.close()
        
    def Writer_File(self, Data_List, Column_Name_List = None): #Escreve no arquivo
        """
           Sua função é escrever no arquivo
           
           Parametro Column_Name_List -> titulos das colunas, por padrao vem none, que nao precisa inserir
           Parametro Data_List -> Uma Lista contendo Listas do que sera escrito em cada Linha
        """
        Writer = csv.writer(self.File_Opened, delimiter = ";") #Objeto que permite a escritira no arquivo
        
        if Column_Name_List != None:
            Writer.writerow(Column_Name_List) #Escreve nas primeiras linhas das colunas
        for Item in Data_List:
            Writer.writerow(Item) # Escreve linha por linha baseado na lista passada
        
        
Data = Data_Writer()
Data.File = "Created.csv"
Data.Open_File()
Data.Writer_File([["Jonathan", "2021", "0729362834"], ["Claudio", "2019", "972228237"]], ["Name ", "Date", "ID"])