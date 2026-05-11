import subprocess
import platform

def le_processo(Ping):
    vetor_processo: str = []
    linha: str = ''
    saida: str = ''
    vetor_linha: str = []

    vetor_processo = Ping.split(' ')
    print(vetor_processo)
    linha = ''
    saida = subprocess.Popen(vetor_processo, stdout=subprocess.PIPE)
    linha = saida.stdout.readline().decode('utf-8', errors = 'ignore')

    while (linha != ''):
        linha = saida.stdout.readline().decode('utf-8', errors = 'ignore')
        if ('Mdia' in linha):
            print (linha)
            vetor_linha = linha.split(' ')
            print("Mdia =", vetor_linha[12])


def PING(sistema):
    ping: str = ''
    if (sistema == "Windows"):
        ping = 'ping -4 -n 10 www.google.com.br'
    else:
        ping = 'ping -4 -c 10 www.google.com.br'
    return ping

def name_so():
    system: str = ''
    Ping: str = ''
    system = platform.system()
    return system

def main():
    SO: str = ''
    SO = name_so()
    print(SO)
    Ping = PING(SO)
    le_processo(Ping)



    

if (__name__ == '__main__'):
    main()
