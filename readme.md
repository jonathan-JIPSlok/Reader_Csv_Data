# Um Leitor de arquivo CSV
***
* O arquivo **main.py** utiliza do modulo Reader_Csv conforme o que o usuario pedir

*O modulo Reader_Csv contem a class Data_Separator*
**Ela necessita como parametro o arquivo que sera tratado**

**Metodos**
* Reader_File - Lê o arquivo csv e o devolve como um objeto pronto para ser tratado

* Pegar_Dados - Parametro *Csv_Object* seria o Objeto devolvido pelo **Reader_File**
* Pegar_Dados - Parametro *Linhas* Tanto de linhas a serem lidas, por padrão vem -1 para ler todas as linhas

* Separator_Lines - Parametro *Lista* Recebe uma lista obtida pelo **Pegar_Dados**
* Separator_Lines - separa linha por linha do arquivo e cria listas com elas

* Close_File - Fecha o arquivo que é algo essencial a se fazer

* Reader_Data_Separator - agiliza o proceso para você, ele pega *Reader_File*, *Pegar_Dados* e *Separator_Lines* e devolve o arquivo já separado linha por linha
* Reader_Data_Separator - Parametro - *Lines_Data* Seria o tando de lonhas a serem lidas

* Print_Detalhing - imprime na tela todos os dados de acordo com o que lhe foi passado
* Print_Detalhing - Parametro - *Data* - os dados prontos para serem impressos
* Print_Detalhing - Parametro - *Information* - por padrão vem "ALL" para pegar todos os dados, passa para ele o que você procura que ele dara todas as linhas que tem este dado