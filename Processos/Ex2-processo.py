import subprocess
import platform

def matar_nome(system, nome):
    processo: str = ''
    vetor_proc: str = []

    if(system == "Windows"):
        processo = f'TASKKILL /IM ' + nome
    else:
        processo = 'pkill -f ' + nome

    vetor_proc = processo.split(' ')
    print(vetor_proc)
    subprocess.run(vetor_proc)


def matar_PID(system, PID):
    processo: str = ''
    vetor_proc: str = []
    pid: str = ''
    pid = str(PID)

    if(system == "Windows"):
        processo = 'TASKKILL /PID ' + pid
    else:
        processo = 'kill -9 ' + pid

    vetor_proc = processo.split(' ')
    print(vetor_proc)
    subprocess.run(vetor_proc)


def listar_processos(system):
    processo: str = ''
    vetor_proc: str = []

    if (system == "Windows"):
        processo = 'TASKLIST /FO TABLE'
    else:
        processo = 'ps -ef'
    
    vetor_proc = processo.split(' ')
    print(vetor_proc)
    subprocess.run(vetor_proc)


def so():
    System: str = ''
    System = platform.system()
    return System

def main():
    system: str = ''
    numero: int = ''
    system = so()
    processo: str = 0
    PID: int = 0
    name: str = ''


    while (numero != 9):
        numero = int(input('\nselecione um dos quatro valores: \n1 - listar os processos \n2 - matar por PID \n3 - matar por nome \n9 - encerrar a aplicação \n \nDigite um número: '))

        if (numero == 1):
            listar_processos(system)

        elif (numero == 2):
            PID = int(input("Digite o PID para matar: "))
            matar_PID(system, PID)
                
        elif (numero == 3):
            nome = str(input("Digite o nome do processo: "))
            matar_nome(system, nome)
       
if __name__ == '__main__':
    main()
