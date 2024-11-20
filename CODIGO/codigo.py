from data import *

#------------------------------------------------------
#Datos
#------------------------------------------------------

#Los beneficios ocurren en hora punta
duracion_hora_punta = 2*6*36 #horas al dia, por 5 dias a la semana, por 36 semanas al año
tasa_ocupacion_auto = 1.5 #persona por vehiculo
duracion_detencion = 45 #segundos cada demora
rugosidad = 1 #por simplicidad
velocidad_crucero = 40 #km/h

#https://sni.gob.cl/storage/docs/Informe_precios_sociales_2024_SNI-Chile.pdf
valor_tiempo_viaje = 3114 #$/h
valor_combustible = 804 #$/L
costo_movimiento = 68.9/ 1000 #L/km
costo_detencion = 8.16/ 1000 #L/det
consumo_total = 1.2 #L/km
consumo_lubricante = 1.109 + 0.005498 * rugosidad
valor_lubricante = 8081
consumo_neumaticos = 0.052 + 0.001241*rugosidad
valor_neumaticos = 74114
consumo_repuestos = 0.173 + 0.00286*(rugosidad**1.87)
valor_repuestos = 113905965
consumo_mano_obra = 1.083 + 0.02539*(rugosidad**1.74)
valor_mano_obra = 6467

#------------------------------------------------------
#Evaluacion social previo a la mejora y posterior a la mejora
#------------------------------------------------------

#Precio del tiempo
#Para cada arco debo calcular los costos que implica

def calcular_cti(row):
    return tasa_ocupacion_auto * row['costo aprox. [h]'] * row['flujo [veh]'] * valor_tiempo_viaje * duracion_hora_punta

# Aplicar la función a cada fila del DataFrame
asignacion_por_arcos['CTi'] = asignacion_por_arcos.apply(calcular_cti, axis=1)
mejora_propuesta['CTi'] = mejora_propuesta.apply(calcular_cti, axis=1)

#Precio del combustible
#Para cada arco debo calcular los costos que implica
def calcular_cc(row):
    S1 = costo_movimiento * 1
    detenciones = ((row['costo aprox. [h]'] - (1 / velocidad_crucero)) * 3600) / duracion_detencion
    S2 = detenciones * costo_detencion
    demoras = detenciones * duracion_detencion
    S3 = demoras * consumo_total
    CC = (S1 + S2) * row['flujo [veh]'] * valor_combustible * duracion_hora_punta
    return CC

asignacion_por_arcos['CC'] = asignacion_por_arcos.apply(calcular_cc, axis=1)
mejora_propuesta['CC'] = mejora_propuesta.apply(calcular_cc, axis=1)

def calcular_oc(row):
   
    S1 = (consumo_lubricante * valor_lubricante)/1000
    S2 = (consumo_neumaticos * valor_neumaticos)/1000
    S3 = (consumo_repuestos * valor_repuestos)/100000
    S4 = consumo_mano_obra * valor_mano_obra/1000

    OC = (S1 + S2 + S3 + S4) * row['flujo [veh]'] * duracion_hora_punta * 1

    return OC

asignacion_por_arcos['OC'] = asignacion_por_arcos.apply(calcular_oc, axis=1)
mejora_propuesta['OC'] = mejora_propuesta.apply(calcular_oc, axis=1)

def add_difference_column(df1, df2, column_name, df3, new_column_name):

    if column_name not in df1.columns or column_name not in df2.columns:
        raise ValueError(f"La columna '{column_name}' no está en ambos DataFrames.")
    
    # Asegúrate de que los índices de df1 y df2 sean compatibles
    if not df1.index.equals(df2.index):
        raise ValueError("Los índices de los DataFrames no coinciden.")

    # Realiza la resta y agrega al tercer DataFrame
    df3[new_column_name] = df1[column_name] - df2[column_name]
    
    return df3

variacion_costos_por_arco = add_difference_column(asignacion_por_arcos, mejora_propuesta, 'CTi', variacion_costos_por_arco, 'Variacion CTi')
variacion_costos_por_arco = add_difference_column(asignacion_por_arcos, mejora_propuesta, 'CC', variacion_costos_por_arco, 'Variacion CC')
variacion_costos_por_arco = add_difference_column(asignacion_por_arcos, mejora_propuesta, 'OC', variacion_costos_por_arco, 'Variacion OC')



CTi_inicial = asignacion_por_arcos['CTi'].sum()
CC_inicial = asignacion_por_arcos['CC'].sum()
OC_inicial = asignacion_por_arcos['OC'].sum()

CTi_mejora = mejora_propuesta['CTi'].sum()
CC_mejora = mejora_propuesta['CC'].sum()
OC_mejora = mejora_propuesta['OC'].sum()

print('Los costos iniciale spor arco son los siguientes: \n')
print(asignacion_por_arcos)
print('')

print('Los costos de la mejora propuesta por arco son los siguientes: \n')
print(mejora_propuesta)
print('')

print('la variacion de los costos por arco es la siguiente: \n')
print(variacion_costos_por_arco)
print('')

print('La variacion de costo total es:')
print(((CTi_inicial + CC_inicial + OC_inicial) - (CTi_mejora + CC_mejora + OC_mejora)))
print('Es decir, se logra reducir los costos')

print('El costo del proyecto es 1.000.000.000')
print('')
print(((CTi_inicial + CC_inicial + OC_inicial) - (CTi_mejora + CC_mejora + OC_mejora))- 1000000000)
print('Es decir')
print((((CTi_inicial + CC_inicial + OC_inicial) - (CTi_mejora + CC_mejora + OC_mejora))- 1000000000)/1000000,'millones de ganancia en el primer año')









        