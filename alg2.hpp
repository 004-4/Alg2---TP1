#include <fstream>
#include <iostream>
#include <unordered_map>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

// Trie
typedef struct No {
    char verbete;
    int indice = 0;
    int fimdopadrao = 0;
    vector<No*> filhos;
} No;

void insere (No* dicio, char caractere, int indice);
No* busca (No* raiz, char caractere);
void comprime (string e, string s);
void descomprime (string e, string s);