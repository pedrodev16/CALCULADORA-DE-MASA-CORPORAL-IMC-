
# Menú principal
data_menu = [
    'VER LOS RANGOS IMC PRECIONE  (R):',
    'PARA CALCULAR  IMC PRECIONE (C):',
    '¿Deseas realizar otra acción? (y/n):'
]
autor = {
    'nombre': 'Laura',
    'apellido': 'Laura',
    'email':'Laura@gmail.com'
    
}
data_autor= autor['nombre']+" Email:"+autor['email']
#lista TABLAS O ARREGLO  DE DIAGNOSTICOS 
data_diagnostico=[
'Criterio de ingreso en hospital',
'Infrapeso',
'Bajo peso',
'Peso normal (saludable)',
'Sobrepeso (obesidad de grado I)',
'Sobrepeso crónico (obesidad de grado II)',
'Obesidad premórbida (obesidad de grado III)',
'Obesidad mórbida (obesidad de grado IV)'
]
            #DICCIONARIO
# Definir la tabla como un diccionario
tabla_imc = {
    "<18.5": "Bajo peso",
    "18.5–24.9": "Peso normal",
    "25.0–29.9": "Pre-obesidad o Sobrepeso",
    "30.0–34.9": "Obesidad clase I",
    "35.0–39.9": "Obesidad clase II",
    "≥40": "Obesidad clase III"
}
def funcion_pendiente():
    pass  # Aquí irá la lógica en el futuro

def ver_rangos_imc():
    print('             _______________                ')
    print('____________|  RANGOS  IMC  |_________________')
    # Aquí puedes implementar la lógica para mostrar los rangos de IMC
      # Iterar sobre las claves y valores del diccionario
    for rango_imc, estado in tabla_imc.items():
        print(f"Rango IMC: {rango_imc} - Estado: {estado}")
    # ...
    
    print('__________________________________________________________')
    print('')
    
def categorizar_peso(p,a):
      # Crear una tupla [DATOS DE CONDICION IMC]
      mi_tupla_IMC = (16,17,18,25,30,35,40)
      
       # Ejemplo de llamada a la función carcular_imc()
      imc = calcular_imc(p,a)

      if imc < mi_tupla_IMC[0]:  
              return data_diagnostico[0]
      
      elif mi_tupla_IMC[0] <= imc < mi_tupla_IMC[1]:
              return data_diagnostico[1]
      
      elif mi_tupla_IMC[1] <= imc < mi_tupla_IMC[2]:        
              return data_diagnostico[2]
      
      elif mi_tupla_IMC[2] <= imc < mi_tupla_IMC[3]: 
               return data_diagnostico[3]
      
      elif mi_tupla_IMC[3] <= imc < mi_tupla_IMC[4]: 
                return data_diagnostico[4]
      
      elif mi_tupla_IMC[4] <= imc < mi_tupla_IMC[5]:  
              return data_diagnostico[5]
      
      elif mi_tupla_IMC[5] <= imc < mi_tupla_IMC[6]:      
               return data_diagnostico[6]
      else:
              return data_diagnostico[7]
def calcular_imc(p,a):
        return p / (a * a)

def calculadora_imc():
    # Aquí Los resultados de la calculadora
    print('             _______________                ')
    print('____________|CALCULADORA IMC|_________________')
    peso = float(input("Ingresa tu peso en kg: "))
    altura = float(input("Ingresa tu altura en metros: "))
    imc = calcular_imc(peso,altura)
    print(f"Tu IMC es: {imc:.2f}")
    print("-->Categoría de peso:", categorizar_peso(peso,altura))
    print('-----------------------------------------')

# Menú principal
data_menu = [
    '-->VER LOS RANGOS IMC PRECIONE  (R):',
    '-->PARA CALCULAR  IMC PRECIONE (C):',
    '-->¿Deseas realizar otra acción? (y/n):'
]

while True:
    for opcion in data_menu:
        print(opcion)
    
    seleccion = input("Selecciona una opción: ").upper()

    if seleccion == 'R':
        ver_rangos_imc()

    elif seleccion == 'C':
        calculadora_imc()
    elif seleccion == 'N':
        print("¡Hasta luego!")
        print("autor:",data_autor)
        break
    else:
        print("_______________-_____________________")
        print("Opción no válida. Inténtalo de nuevo.|")
        print("_____________________________________")
        continue  # Continuar con la siguiente iteración

 
    # Si no necesitas hacer nada en particular, puedes usar 'pass' para omitir esta parte

else:
    
    print("¡Gracias por usar el programa!")
