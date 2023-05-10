import csv
import os
import time
from os import system

folder = 'C:\\Users\\HP\\Documents\\IA-PIA\\IA- PIA\\'    #   DIRECCION DEL FOLDER "\\low-dimensional"
datos = []

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
    tareasRealizar = []
    valorSubtema = [0, 0, 0, 0, 0, 0, 0, 0]
    duracionSubtema = [0, 0, 0, 0, 0, 0, 0, 0]

    for subtemaID in range(1, 9, 1):

        for tareaID in range(1, 12, 1):

            if(datos[5][tareaID + subtemaA - 1] == 1):

                tareasRealizar.append(tareaID + subtemaA)
                valorSubtema[datos[1][tareaID + subtemaA- 1] - 1] += datos[4][tareaID + subtemaA - 1]
                duracionSubtema[datos[1][tareaID + subtemaA- 1] - 1] += datos[3][tareaID + subtemaA - 1]

                if(datos[6][tareaID + subtemaA - 1] != 0):

                    tareasRealizar.append(datos[6][tareaID + subtemaA - 1])
                    valorSubtema[datos[1][datos[6][tareaID + subtemaA- 1]] - 1] += datos[4][datos[6][tareaID + subtemaA - 1]]
                    duracionSubtema[datos[1][datos[6][tareaID + subtemaA- 1]] - 1] += datos[3][datos[6][tareaID + subtemaA - 1]]
                    
                if(datos[7][tareaID + subtemaA - 1] != 0):

                    tareasRealizar.append(datos[7][tareaID + subtemaA - 1])
                    valorSubtema[datos[1][datos[7][tareaID + subtemaA]] - 1] += datos[4][datos[7][tareaID + subtemaA - 1]]
                    duracionSubtema[datos[1][datos[7][tareaID + subtemaA]] - 1] += datos[3][datos[7][tareaID + subtemaA - 1]]

        for tareaF in range(1, 12, 1):

            if(valorSubtema[subtemaID - 1] >= 70):

                tareaF = 12

            else:
                
                if((tareaF + subtemaA) not in tareasRealizar):

                    tareasRealizar.append(tareaF + subtemaA)
                    valorSubtema[subtemaID - 1] += datos[4][tareaF + subtemaA - 1]
                    duracionSubtema[subtemaID - 1] += datos[3][tareaF + subtemaA - 1]

        subtemaA += 11

    print(valorSubtema)
    print(duracionSubtema)
    print(tareasRealizar)
    
start_time = time.time()

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

runtime = time.time() - start_time
print("Runtime: " + str("{:.15f}".format(runtime)) + "\n")