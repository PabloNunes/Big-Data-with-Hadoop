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
    * *Para manipular o arquivo fazemos:
      * `arquivo.write('Coisas aqui')`
    * Não esqueça de fechar para não colocar coisas indesejáveis no seu arquivo:
      * `arquivo.close`
    
  
    
  
