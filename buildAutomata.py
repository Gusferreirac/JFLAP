from automata.fa.nfa import NFA
from automata.fa.dfa import DFA
import json

afd = ""
afn = ""

def afdBuild(filePath):
    with open(filePath) as file:
        afdRead = file.read()
        afdObject = json.loads(afdRead) #Transforma o arquivo JSON em um objeto

    #Cria o afd globalmente para a funcao de teste ter acesso
    global afd
    afd = DFA(
        states=set(afdObject["states"]),
        input_symbols=set(afdObject["input_symbols"]),
        transitions=afdObject["trasitions"],
        initial_state=afdObject["initial_state"],
        final_states=set(afdObject["final_states"])
    )

    afd.show_diagram(path='./automata.png') #Gera a imagem do automato que sera mostrada na janela

def afnBuild(filePath):
    with open(filePath) as file:
        afnRead = file.read()
        afnObject = json.loads(afnRead)
        dictionary = afnObject["trasitions"]

        #Funcao para converter o dicionario de transicoes no formato certo
        #Os valores dos estados que serao ativados dever ser um set pois um caractere pode ativar multiplos estados
        for i in dictionary:
            for key, value in zip(dictionary[i].keys(), dictionary[i].values()):
                dictionary[i][key] = set(value)

    # Cria o afn globalmente para a funcao de teste ter acesso
    global afn
    afn = NFA(
        states= set(afnObject["states"]),
        input_symbols=set(afnObject["input_symbols"]),
        transitions=dictionary,
        initial_state=afnObject["initial_state"],
        final_states=set(afnObject["final_states"])
    )

    afn.show_diagram(path='./automata.png') #Gera a imagem do automato que sera mostrada na janela

def afdRun(word):
    return afd.accepts_input(word) #Verifica se a palavra esta no conjunto de palavras aceitas

def afnRun(word):
    return afn.accepts_input(word) #Verifica se a palavra esta no conjunto de palavras aceitas