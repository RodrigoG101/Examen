import random
import csv

trabajadores = ['Juan Pérez','María García','Carlos López','Ana Martínez','Pedro Rodríguez','Laura Hernández','Miguel Sánchez','Isabel Gómez','Francisco Díaz','Elena Fernández']
lista_trabajadores =[]
menores = []
medios = []
mayores = []

def InsertarSueldo():
    for i in trabajadores:
        lista_trabajadores.append({'nombre':i,'sueldo':random.randint(300000,2500000)})
    print('Sueldos insertados correctamente')

def ClasificarSueldos():
    if not lista_trabajadores: return print('Error, sueldos no asignados')
    suma_sueldos = 0
    for i in lista_trabajadores:
        suma_sueldos+=i['sueldo']
        if i['sueldo']<800000: menores.append(i)
        elif i['sueldo']>= 800000 and i['sueldo']<= 2000000: medios.append(i)
        elif i['sueldo']> 2000000: mayores.append(i)
    
    print(f'''
    Sueldos menores a 800.000 Total: {len(menores)}
Nombre Empleados    Sueldo''')
    for i in menores:
        print(f'{i["nombre"]}      {i["sueldo"]}')
    print(f'''
    Sueldos entre 800.000 y 2.000.000 Total: {len(medios)}
Nombre Empleados    Sueldo''')
    for i in medios:
        print(f'{i["nombre"]}      {i["sueldo"]}')
    print(f'''
    Sueldos mayores a 2.000.000 Total: {len(mayores)}
Nombre Empleados    Sueldo''')
    for i in mayores:
        print(f'{i["nombre"]}      {i["sueldo"]}')
    print(f'Total Sueldo Empleados: {suma_sueldos}')

def VerEstadistica():
    if not lista_trabajadores: return print('Error, sueldos no asignados')
    sueldo_menor = 2000000 # Temporal Arreglar
    sueldo_mayor = 0
    sueldo_total = 0
    for i in lista_trabajadores:
        sueldo_total+= i['sueldo']
        if sueldo_menor > i['sueldo']:
           sueldo_menor = i['sueldo']

        if sueldo_mayor < i['sueldo']:
            sueldo_mayor = i['sueldo']
    sueldo_total = i['sueldo']/len(lista_trabajadores)
    print(f'''
          Sueldo Meno: ${sueldo_menor}
          Sueldo Mayor ${sueldo_mayor}
          Sueldo Promedio ${(sueldo_menor+sueldo_mayor)/2}
          Media Geometrica: ${sueldo_total}''')

def ReporteSueldo():
    if not lista_trabajadores: return print('Error, sueldos no asignados')
    listacsv = []
    print('Nombre empleado | Sueldo base | Descuento Salud | Descuento AFP | Sueldo Liquido')
    for i in lista_trabajadores:
        desc_salud = int(i['sueldo']*0.07)
        desc_afp = int(i['sueldo']*0.12)
        sueldo_liquido = int(i['sueldo']-(desc_salud+desc_afp))
        
        listacsv.append([i['nombre'],i['sueldo'],desc_salud,desc_afp,sueldo_liquido])
        print(f'''{i['nombre']}       ${i['sueldo']}       ${desc_salud}           ${desc_afp}         ${sueldo_liquido}''')
   # Crear CSV
    with open ('Trabajadores.csv','w', newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(['Nombre empleado | Sueldo base | Descuento Salud | Descuento AFP | Sueldo Liquido'])
        for i in listacsv:
            nombre = i[0]
            sueldo = i[1]
            descsalud = i[2]
            descafp = i[3]
            sueldoliquido = i[4]
            escritor.writerow({nombre,sueldo,descsalud,descafp,sueldoliquido})

def Menu():
    print('''
1. Asignar sueldos aleatorios
2. Clasificar sueldos
3. Ver estadísticas.
4. Reporte de sueldos
5. Salir del programa
''')

while True:
    Menu()
    
    while True:
        opc = input('ingrese una opcion: ')
        if opc.isnumeric() == True:
            opc = int(opc)
            if opc >=1 and opc<=5:
                break
            else: print('Error,opcion no valida')
        else: print('Error,ingrese numero')

    if opc == 1: InsertarSueldo()
    elif opc == 2: ClasificarSueldos()
    elif opc == 3: VerEstadistica()
    elif opc == 4: ReporteSueldo()
    elif opc == 5: 
        print('''
Finalizando Programa...
Desarrollado por Rodrigo Gomonal
Rut 19430227-4
''')
        break