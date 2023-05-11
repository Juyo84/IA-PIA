import csv
import os
import time
from os import system

folder = 'C:\\Users\\User\\OneDrive - uanl.edu.mx\\Documents\\Archivos FCFM\\Actividades\\6° Sem\\IA\\IA_PIA\\IA-PIA\\'    #   DIRECCION DEL FOLDER "\\low-dimensional"
datos = []
tareasRealizar = []
valorSubtema = [0, 0, 0, 0, 0, 0, 0, 0]
duracionSubtema = [0, 0, 0, 0, 0, 0, 0, 0]
carreo = [0, 0, 0, 0, 0, 0, 0, 0]

system("cls")   #   LIMPIA LA TERMINAL

#LEE LAS INSTANCIAS DEL ARCHIVO
def asignar_Instancias(filename):
   print('____________________________________________________'+filename+' ____________________________________________________')
   nodo = []
   subtema = []
   tarea = []
   duracion = []
   valor = []
   obligatorio = []
   requerimiento1 = []
   requerimiento2 = []
   n = 0
   with open(folder+ 'low-dimensional\\' + filename, 'rt') as f:
      reader = csv.reader(f)
      for row in reader:
         if(len(row)>0):
            if(row[0] != ''):
               n += 1
               nodo.append(n)
               subtema.append(int(row[2]))
               tarea.append(int(row[3]))
               duracion.append(int(row[4]))
               valor.append(int(row[5]))
               obligatorio.append(int(row[9]))
               requerimiento1.append(int(row[7]))
               requerimiento2.append(int(row[8]))
   return(list([nodo, subtema, tarea, duracion, valor, obligatorio, requerimiento1, requerimiento2]))


def algoritmo(datos):
    
    subtemaA = 0
    #tareasRealizar = []
    #valorSubtema = [0, 0, 0, 0, 0, 0, 0, 0]
    #duracionSubtema = [0, 0, 0, 0, 0, 0, 0, 0]

    for tareaID in range(0, 88, 1):
        if(datos[5][tareaID] == 1):
            agregarRequisito(tareaID)

            carreo = [0, 0, 0, 0, 0, 0, 0, 0]

    for subtemaID in range(1, 9, 1):
        for tareaF in range(1, 12, 1):

            if(valorSubtema[subtemaID - 1] >= 70):

                break

            else:
                
                #Revisar que esa Tarea no esté dentro con anterioridad.
                if((tareaF + subtemaA) not in tareasRealizar):

                    if(checarRequisito(tareaF + subtemaA - 1) == True):
                        agregarRequisito(tareaF + subtemaA - 1)

                    carreo = [0, 0, 0, 0, 0, 0, 0, 0]
        subtemaA += 11

    tareasRealizar.sort()
    print(valorSubtema)
    print(duracionSubtema)
    print(tareasRealizar)
    
start_time = time.time()


def checarRequisito(tarea):
    check1 = True
    check2 = True

    if((tarea + 1) in tareasRealizar):
        return True
    else:
        if((datos[4][tarea] + carreo[datos[1][tarea] - 1]) >= 100 or 
           valorSubtema[datos[1][tarea] - 1] >= 70):
            return False
        else:
            carreo[datos[1][tarea] - 1] += datos[4][tarea]

            if(datos[6][tarea] != 0):
                check1 = checarRequisito(datos[6][tarea] - 1)
            if(datos[7][tarea] != 0):
                check2 = checarRequisito(datos[7][tarea] - 1)

            if(check1 and check2):
                return True
            else:
                return False

def agregarRequisito(tarea):

    if((tarea + 1) not in tareasRealizar):
        if(datos[6][tarea] != 0):
            agregarRequisito(datos[6][tarea] - 1)
        if(datos[7][tarea] != 0):
            agregarRequisito(datos[7][tarea] - 1)

        tareasRealizar.append(tarea + 1)
        valorSubtema[datos[1][tarea] - 1] += datos[4][tarea]
        duracionSubtema[datos[1][tarea] - 1] += datos[3][tarea]

#REALIZA n ITERACIONES
for iteraciones in range(0,1,1):
    
    for filename in os.listdir(folder + 'low-dimensional\\'):
        if filename.endswith(".csv"):
            nombre = filename.split('_')
            datos = asignar_Instancias(filename)    #  PASAMOS LAS INSTANCIAS A UNA VARIABLE
            
            resultado = algoritmo(datos)
            
            #SE IMPRIME LOS RESULTADOS
            #print("-------------------------------------------------------------------------")
            #print("Capacidad: " + str("{:.4f}".format(resultado[0])) + "      Beneficio: " + str("{:.4f}".format(resultado[1])) + "       Nodos: "
            #      + str(resultado[2]))
            
            datos = []
            tareasRealizar = []
            valorSubtema = [0, 0, 0, 0, 0, 0, 0, 0]
            duracionSubtema = [0, 0, 0, 0, 0, 0, 0, 0]
            carreo = [0, 0, 0, 0, 0, 0, 0, 0]

runtime = time.time() - start_time
print("Runtime: " + str("{:.15f}".format(runtime)) + "\n")
