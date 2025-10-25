class Solution:
    def reverseVowels(self, s: str) -> str:
        vocales = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        lista_palabra =  list(s)
        lista_vocales = []
        for i in lista_palabra:
            if i in vocales:
                lista_vocales.append(i)

        len_vocales = len(lista_vocales)
        len_vocales -= 1
        cadena = ""
        x = 0

        for i in lista_palabra:

            if i in vocales:
                lista_palabra[x] = lista_vocales[len_vocales]
                len_vocales -= 1

            cadena += lista_palabra[x]
            x += 1
        return cadena
# End-of-file (EOF)
