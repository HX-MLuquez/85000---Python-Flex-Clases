import sys


list_args = sys.argv[1:] # args de la línea de comandos sin el nombre del script

print(list_args) # args de la línea de comandos


print('Hola mundo')

if len(list_args) > 0:
    if list_args[0] == 'mode:dev':
        print('Modo de desarrollo activado')
    elif list_args[0] == 'mode:prod':
        print('Modo de producción activado')
    