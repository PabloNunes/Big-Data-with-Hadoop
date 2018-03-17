# **Curso Big Data com Hadoop - Dia 10/03 - Tarde**
## Python
  * O # serve para fazer comentários
  * O operador `a**b` = a elevado a b
  * O operador `a%b` = a mod b (resto)
  * O Python é uma linguagem dinamicamente tipada. Ou seja, não precisa tipar as variáveis.
  * **String em Python**:
    * Vamos supor a variável -> word = 'algomaneiro'
    * `word[1] = l`
    * `2*word[3] = oo`
    * `word[1:5:2] = lo` -> *Da posição de 1 a 5 com incremento de 2*
    * `word [::-1] = orienamogla` -> *Leu a palavra invertida com passos de -1*
    * `word [::-2] = oinmga` -> *Leu a palavra invertida com pulos de 2*
    * `word [::-11] = o` -> *Leu a primeira letra invertida (ou seja leu ao contrário) e pulou o resto todo*
  * **Lista em Python**:
    * Podemos usar uma variável para colocar uma lista -> `lista = [1,2,3]`
    * Acessando uma variável dentro de uma lista -> `lista[0] = 1`
    * Podemos somar elementos de uma lista como variáveis normais -> `lista[0]+lista[2] = 4`
    * Podemos colocar elementos da lista -> `lista = lista + [4] -> [1,2,3,4] -> lista = lista + [0,0,0]`
    * Podemos ler a lista sendo invertida -> `lista[-1] = 0`
    * Podemos ler vários elementos da lista com : -> `lista[2:-2] = [3,4,0]`
    * Podemos substituir variáveis internamente na lista -> `lista[0] = 'zero' -> lista = ['zero',2,3,4,0,0,0]`
  * **Matriz em Python**:
    * Vamos fazer várias linhas -> `linha_1 = [1,2,3], linha_2 = [0,-1,1], linha_3 = [3,3,3]`
    * Gerando a matriz -> `matriz = [linha_1,linha_2,linha_3]`
    * Acessando a matriz -> `matriz[0] = [1,2,3], matriz[[1],[2]] = -1`
  * **Tuplas em Python**:
    * Tuplas são objetos parecidos com lista mas são imutáveis -> `tupla = (1,2,3) -> tupla[1] = 2`
  * **Packing-Unpacking**:
    * É uma função para inferir as variáveis como chave valor:
      * `a,b = 1,2`
      * `a = 1, b = 2`
  * **Entrada de dados**:
    * O uso para entrada de dados simples -> `input("Pergunta aqui")`
  * **Loop condicional**:
    * O for serve para loopar uma sequencia de instruções até acabar a contagem do laço `a = [1,2,3] -> for i in a:`
      * *Neste caso i vai assumir todos os valores em a.*
  * **Range**:
    * O range serve para fazer uma lista com sequência com diversas condições.
    * `range(0,9) = [0,1,2,...,9]`
  * **Dicionário**:
    * Usa chave-valor para uma chave equivaler a um valor ao retornar
    * `Dic = {'meme':2000}`
  * **Funções**:
    * Você pode fazer funções com `def nome_da_funcao (variaveis,de, entrada)`.
    * `def f(x)`
  * **Importar bibliotecas**:
    * O import pode importar bibliotecas para poder usar várias funções do python e bibliotecas fora dele para poder implementar funcionalidades novas.
    * `import math`
    * `math.pi` -> *É o pi!*
  * **Manipulação de Arquivos**:
    * Podemos usar o open e seus modos para mainpular arquivos de dados. -> `variavel = open('nome.extensao, modos)`
    * Os modos são:
      * `a -> append (Abre o arquivo, não deleta, bota mais)`
      * `w -> write (Abre o arquivo, deleta antigo, reescreve)`
      * `r -> read (Só le)`
    * Para manipular o arquivo fazemos:
      * `arquivo.write('Coisas aqui')`
    * Não esqueça de fechar para não colocar coisas indesejáveis no seu arquivo:
      * `arquivo.close`
## R
  * **Atribuir Números**
    * Para atribuir a x um número: `x <- 8` ou `x = 8` ou `8 <- x`
  * **Comando Seq**
    * Produz sequencias com incio, fim e passo
    * `seq(1,10,1) - 1 2 3 ... 10`
    * `seq(1,10,2) - 1 3 5 ... 9`
    * Produz sequencias reversas
    * `seq(10,1,-3) - 10 7 4 1`
  * **Comando Rep**
    * Retorna o primeiro argumento pelo número indicado na segunda posição
    * `rep(1,10)` -> `1 1 1 1 ... 1` - *10 vezes 1*
  * **Comando Lista**
    * A lista permite a combinações de diferentes tipos de objetos dentro de um mesmo objeto.
    * `R <- list(versao=2.4,origem='Austrália',notas=c(10,9,5))R`
  * **Comando names**
    * Mostra todas as caracteristicas que algo possui
    * `names(x)` -> mostra o que tem em x
  * **Função**
    * Pode-se criar uma função em R com um nome não ocupado e fazer uma função
    * `media <- function(dados)
      {
      print(sum(dados)/length(dados))
      }`
  * **Medidas de dispersão amostral**
    * `var(x)` -> *Variância*
    * `sd(x)` -> *Desvio Padrão*
    * `max(x) - min(x)` -> *Amplitude Total*
    * `sd(x)/sqrt(length(x))` -> *Erro padrão da média*
    * `sd(x)/mean(x)*100` -> *Coeficiente de variação*
  * **Teste T**
    * É usado para comparar várias médias com amostragens diferentes.
## Pig
  * **Descrição**
    * É chamada de Pig pois ele é adaptado para "comer" um monte de dados e de MUITOS tipos.
    * Se usa o Pig Latin
    * O Pig Latin usam os scripts escritos a eles e os convertem em mapas.
    * O Pig diminui o tempo de desenvolvimento em 16 vezes.
    * É muito similar ao SQL.
    * Fornece vários comandos internos para a dados e suas operações
  * **Diferenças do Pig vs SQL**

|Pig|SQL|
|:---------------------------------------------------------------:|:----------------------------------------------:|
|É processual|É declarativo|
|O esquema é opcional. Pode armazenar dados sem projetar esquema|O esquema é obrigatório|
|É alinhado relacional|É plano relacional|
|Menos possibilidade de otimização de consultas| Mais possibilidades de otimização de consultas 	|

  * **Recursos do Apache Pig**
    * **Extensibilidade**
      * Os usuários podem usar suas próprias funções para ler, processar e gravar dados.
    * **UDF'S**
      * Facilidade para criar funções definidas pelo usuário em outras linguagens de programação
    * **Manipula todos os tipos de dados**
      * Analisa todos os tipos de dados, estruturados ou não e armazena no HDFS
    * **Conjunto Rico de Operadores**
      * Fornece muitos operadores para executar operações (Juntar, Classificar, Filter)
    * **Facilidade de programação**
      * PIG Latin é semelhante ao SQL
    * **Otimização de oportunidades**
      * As tarefas se otimizam automáticamente no PIG
     



    
  
    
  
