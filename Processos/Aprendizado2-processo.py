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


    #system = platform.system()
    #release = platform.release()
    #version = platform.version()
    #arch = platform.architecture()

    #print(system, release, version, arch)

def main():
    #prop_os()

    processo: str = ''
    processo = 'tasklist'
    abre_processo(processo)

if __name__ == '__main__':
    main()
