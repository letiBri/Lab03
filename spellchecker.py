import time

import multiDictionary as md

class SpellChecker:

    def __init__(self):
        pass

    def handleSentence(self, txtIn, language):
        start = time.time()
        txtIn.lower()
        txtFin = replaceChars(txtIn)
        multiDizionario = md.MultiDictionary()
        multiDizionario.printDic(language)
        #listaReachWords = multiDizionario.searchWordLinear(txtFin, language)
        listaReachWords = multiDizionario.searchWordDichotomic(txtFin, language)
        myStr = ""
        print("Using contains")
        for word in listaReachWords:
            if word.corretta is False:
                myStr += f"\n{word}"
        print(myStr[1::])
        end = time.time()
        print(end - start)


    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\'*_{}[]()>#+-.!$%^;,=_"
    for c in chars:
        text = text.replace(c, "")
    return text

