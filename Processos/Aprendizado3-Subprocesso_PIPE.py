import platform
import subprocess

#def prop_os():  #procedimento
    #system: str = ''
    #release: str = ''
    #version: str = ''
    #arch: str = ''

def abre_processo(processo):
    vetor_processo: str = [] #abrimos um vetor para separar cada elemento do comando por vírgulas, não havendo erros.
    vetor_processo = processo.split(' ') #split quebra, reparte. Aqui ele faz isso pro espaços.
    print(vetor_processo)
    subprocess.run(vetor_processo)

def le_processo(processo):
    vetor_processo: str = []
    linha: str = ''  #usamos porque a saída do nosso processo ocorrerá linha a linha. Dessa forma, podemos fazer outras coisas com ela, como um if, teste, content (In).
    saída: str = ''

    vetor_processo = processo.split(' ')
    print(vetor_processo)
    linha = '' 
    saída = subprocess.Popen(vetor_processo, stdout=subprocess.PIPE) #P OPEN (abrir processo). Aqui, nós abrimos o vetor_processo com uma saída padrão no formato de subprocess.PIPE. Estamos fazendo um PIPE
    #A linha a seguir serve para não dar erro no while!
    linha = saída.stdout.readline().decode('utf-8', errors = 'ignore') #Lê uma linha da saída do processo (saída.stdout.readline()). Transforma em texto normal (.decode('utf-8')). Ignora caracteres invalidos (errors='ignore').

    while (linha != ''):
        #print(linha)
        if ("Diretrio" in linha):
            print(linha)
        linha = saída.stdout.readline().decode('utf-8', errors = 'ignore')


    #system = platform.system()
    #release = platform.release()
    #version = platform.version()
    #arch = platform.architecture()

    #print(system, release, version, arch)

def main():
    #prop_os()

    processo: str = ''
    processo = 'systeminfo'
    #abre_processo(processo)
    le_processo(processo)

if __name__ == '__main__':
    main()
