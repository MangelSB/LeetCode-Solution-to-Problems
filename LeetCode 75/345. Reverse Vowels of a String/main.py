class Solution:
    def reverseVowels(self, s: str) -> str:
        vocales = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        listaPalabra =  list(s)
        listaVocales = []
        for i in listaPalabra:
            if(i in vocales):
                listaVocales.append(i)

        lenVocales = len(listaVocales)
        lenVocales -= 1
        cadena = ""
        x = 0

        for i in listaPalabra:

            if(i in vocales):
                listaPalabra[x] = listaVocales[lenVocales]
                lenVocales -= 1

            cadena += listaPalabra[x]
            x += 1
    
        return(cadena)  