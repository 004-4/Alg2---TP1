#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

// Trie
typedef struct No {
    char verbete;
    int indice = 0;
    int fimdopadrao = 0;
    vector<No*> filhos;
} No;

//insere na árvore a tupla (indice do nó anterior, caractere) e marca o índice separado daquele filho
void insere (No* dicio, char caractere, int indice);

//busca na árvore se o caractere passado já está presente em algum padrão
No* busca (No* raiz, char caractere);

//passa o texto lido para um outro arquivo o codificando segundo os padrões inseridos na árvore
void comprime (string e, string s);

//o indice da tupla permite que os caracteres anteriores sejam encontrados e concatenados ao atual, reconstruindo o texto
void descomprime (string e, string s);
