#CONTEXTO
#criando um algoritmo que o MCdonalds usa
#a interface das maquinas preve a leitura de um arquivo texto no formato: QUANTIDADE, PRODUTO, TAMANHO

import speech_recognition as sr
import nltk
from nltk.corpus import mac_morpho  #corpus=documento,  mac_morpho=documento em portugues
from nltk.tag import tnt
from nltk import tokenize

nltk.download('mac_morpho')

#funcao responsavel por ouvir e reconhecer a fala
def fazerPedido():

    #habilita o microfone para ouvir o usuario
    microfone = sr.Recognizer()

    with sr.Microphone() as source:

        #chama a funcao de reducao de ruido disponivel na speech_recognition
        microfone.adjust_for_ambient_noise(source)

        #avisa o usuario que esta pronto para ouvir 
        print("Faca o seu pedido: ")

        #armazena a informacao de audio na variavel
        audio = microfone.listen(source)

    try:
        #passa o audio para o reconhecedor de padroes do speech_recognition
        frase = microfone.recognize_google(audio, language='pt-BR')
        return frase

    #caso nao tenha reconhecido o padrao de fala, exibe esta mensagem
    except sr.UnknownValueError:
        print("Infelizmente nao entendi seu pedido. Repita seu pedido, por favor")


#TREINANDO O POS-TAGGER
tagged_sents = mac_morpho.tagged_sents()  #mostra todo o texto do macmorpho com a analise morfologica, guadando na variavel tagged_sents

tnt_pos = tnt.TnT() #instancia 

tnt_pos.train(tagged_sents)

pedido = fazerPedido()
print(pedido)

print(tnt_pos.tag(tokenize.word_tokenize(pedido, language='portuguese')))





