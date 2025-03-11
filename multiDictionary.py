import dictionary as d
import richWord as rw
from resources import *


class MultiDictionary:

    def __init__(self):
        self.multiDict = {}

    def printDic(self, language):
        if language == "english":
            dizInglese = d.Dictionary()
            dizInglese.loadDictionary("resources/English.txt")
            self.multiDict["english"] = dizInglese.dict
        if language == "spanish":
            dizSpagnolo = d.Dictionary()
            dizSpagnolo.loadDictionary("resources/Spanish.txt")
            self.multiDict["spanish"] = dizSpagnolo.dict
        if language == "italian":
            dizItaliano = d.Dictionary()
            dizItaliano.loadDictionary("resources/Italian.txt")
            self.multiDict["italian"] = dizItaliano.dict

    def searchWordLinear(self, words, language):
        parole = words.split(" ")
        dizTrovato = self.multiDict[language]
        listaReachWords = []
        for parola in parole:
            existing = False
            if parola in dizTrovato:
                existing = True
            richWord = rw.RichWord(parola)
            richWord.corretta = existing
            listaReachWords.append(richWord)
        return listaReachWords

    def searchWordDichotomic(self, words, language):
        parole = words.split(" ")
        dizTrovato = self.multiDict[language]
        listaRichWords = []
        inizio = 0
        fine = len(dizTrovato)
        for parola in parole:
            parolaTrovata = False
            while inizio <= fine:
                meta = (inizio + fine) // 2
                parolaCentrale = dizTrovato[meta]
                if parolaCentrale == parola:
                    parolaTrovata = True
                    break
                elif parolaCentrale < parola:
                    inizio = meta + 1
                else:
                    fine = meta - 1
            richWord = rw.RichWord(parola)
            richWord.corretta = parolaTrovata
            listaRichWords.append(richWord)
        return listaRichWords







