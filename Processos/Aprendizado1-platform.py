import platform

def prop_os():  #procedimento
    system: str = ''
    release: str = ''
    version: str = ''
    arch: str = ''

    system = platform.system()
    release = platform.release()
    version = platform.version()
    arch = platform.architecture()

    print(system, release, version, arch)

def main():
    prop_os()

if __name__ == '__main__':
    main()
