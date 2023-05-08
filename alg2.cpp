#include "alg2.hpp"

void insere (No* dicio, char caractere, int indice){
    No* dicioaux = new No();
    dicioaux->verbete = caractere; 
    dicioaux->indice = indice;
    dicio->filhos.push_back(dicioaux);
}
No* busca (No* raiz, char caractere){
    for (auto i : raiz->filhos){
        if (i->verbete == caractere){
            return i;
        } 
    }
    return nullptr;
}
void comprime (string e, string s){
    ifstream entrada(e, ios::binary);
    ofstream saida(s, ios::binary|ios::out);
    No* raiz = new No();
    No* dicio = raiz;
    string line;
    char caractere;
    int indice = 1;
    vector<pair<int, char>> texto;
    while(entrada.get(caractere)){
        No* dicio2 = busca (dicio, caractere); 
        if (dicio2 == nullptr){
            texto.push_back(pair<int, char>(dicio->indice, caractere));
            insere(dicio, caractere, indice);
            dicio = raiz;
            indice++;
        }
        else {
            dicio = dicio2;
        }
    }
    for (auto i : texto){
        saida.write(reinterpret_cast<const char*>(&i.first), sizeof(int));
        saida.write(reinterpret_cast<const char*>(&i.second), sizeof(char));
    }
    saida.write(reinterpret_cast<const char*>(&dicio->indice), sizeof(int));
    saida.close();
    entrada.close();
}
void descomprime (string e, string s){
    ifstream entrada(e, ios::binary);
    ofstream saida(s, ios::binary|ios::out);
    vector<string> texto;
    texto.push_back("");
    int numero;
    while(entrada.read((char*) &numero, sizeof(int))){
        char caractere;
        if (entrada.get(caractere)){
            texto.push_back(texto[numero] + caractere);
        } 
        else break;
    }
    texto.push_back(texto[numero]);
    for (int i = 1; i < texto.size(); i++){
        texto[0] += texto[i];
    }
    saida << texto[0];
}
int main(int argc, char** argv){
    ifstream entrada;
    ofstream saida;
    string out;
    if (argc == 5){
        out = argv[4]; 
    }
    else{
        string in = string(argv[2]);
        out = in.substr(0, in.length() - 3);
        if (string(argv[1]) == "-c") out += "z78";
        else if (string(argv[1]) == "-x") out += "txt";
    }
    if (string(argv[1]) == "-c") comprime (argv[2], out);
    else if (string(argv[1]) == "-x") descomprime (argv[2], out);
}