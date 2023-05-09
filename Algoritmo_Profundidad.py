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
               subtema.append(row[2])
               tarea.append(row[3])
               duracion.append(row[4])
               valor.append(row[5])
               obligatorio.append(row[9])
               requerimiento1.append(row[7])
               requerimiento2.append(row[8])
   return(list([nodo, subtema, tarea, duracion, valor, obligatorio, requerimiento1, requerimiento2]))


#OBTENER f(x) = h(x) + g(x)
def beneficio_peso(datos):

    valor_h = []

    for nodos in range(0, len(datos[0])-1, 1):
        
        valor_h.append((float(datos[4][nodos]) / float(datos[3][nodos])) + float(datos[4][nodos]))

    return valor_h

#SE REALIZA EL ALGORITMO
def algoritmo(valor_h, datos):
    
    nodos_Factibles = []
    nodos = datos[0]
    valorTotal = 0
    duracionTotal = 0







start_time = time.time()

#REALIZA n ITERACIONES
for iteraciones in range(0,1,1):
    
    for filename in os.listdir(folder + 'low-dimensional\\'):
        if filename.endswith(".csv"):
            nombre = filename.split('_')
            datos = asignar_Instancias(filename)    #  PASAMOS LAS INSTANCIAS A UNA VARIABLE
            
            resultado = algoritmo(beneficio_peso(datos), datos)
            
            #SE IMPRIME LOS RESULTADOS
            #print("-------------------------------------------------------------------------")
            print("Capacidad: " + str("{:.4f}".format(resultado[0])) + "      Beneficio: " + str("{:.4f}".format(resultado[1])) + "       Nodos: "
                  + str(resultado[2]))
            
            datos = []

runtime = time.time() - start_time
print("Runtime: " + str("{:.15f}".format(runtime)) + "\n")