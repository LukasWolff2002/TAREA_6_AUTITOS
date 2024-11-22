import pandas as pd

flujos = {
    "A–D": 800,
    "A–E": 400,
    "A–F": 400,
    "B–D": 750,
    "B–E": 600,
    "B–F": 900,
    "C–D": 950,
    "C–E": 700,
    "C–F": 1450
}

data_routes = {
    "par O–D": ["A–D", "A–E", "A–F", "B–D", "B–E", "B–F", "C–D", "C–E", "C–F"],
    "rutas": [
        "a–i–r",
        "a–i–n–s, a–e–j–s",
        "a–i–n–p–m, a–e–j–p–m, a–e–g–k–m, a–e–g–l",
        "b–f–i–r, b–j–o–r",
        "b–j–s",
        "b–j–p–m, b–g–k–m, b–g–l",
        "c–f–i–r, c–j–o–r, d–h–f–i–r, d–h–j–o–r, d–k–q–o–r",
        "c–j–s, d–h–j–s, d–k–q–s",
        "d–k–m, d–l"
    ]
}

df_routes = pd.DataFrame(data_routes)

# Creating a dataframe with the given data
asignacion_por_arcos = {
    "arco": ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s"],
    "flujo [veh]": [1600, 2250, 1255, 1845, 710.31, 610.03, 605.3, 0.02, 1499.72, 3000, 785.28, 1665, 1085, 89.69, 1089.97, 694.7, 394.98, 2500, 1700],
    "costo aprox. [h]": [0.625, 0.15, 0.28, 0.255, 0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 0.135, 0.11, 0.025, 0.025, 0.025, 0.025, 0.275, 0.158]
}

asignacion_por_arcos = pd.DataFrame(asignacion_por_arcos)

flujo_saturacion ={
 'a': 1000,
 'c': 1000,
 'e': 1000,
 'f': 1000,
 'g': 1000,
 'h': 1000,
 'm': 1000,
 'd': 1500,
 'i': 1500,
 'l': 1500,
 's': 1500,
 'b': 2000,
 'k': 2000,
 'n': 2000,
 'o': 2000,
 'p': 2000,
 'r': 2000,
 'j': 3000,
 'q': 3000
}

# Creating a dataframe with the updated data
mejora_propuesta = {
    "arco": ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s"],
    "flujo [veh]": [1600, 2250, 1050, 2050, 710.31, 610.03, 605.3, 102.52, 1499.72, 2897.5, 887.78, 1665, 1085, 89.69, 1089.97, 694.7, 497.48, 2500, 1700],
    "costo aprox. [h]": [0.625, 0.15, 0.075, 0.05, 0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 0.135, 0.11, 0.025, 0.025, 0.025, 0.025, 0.275, 0.158]
}

variacion_costos_por_arco = {
    "arco": ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s"]
}

mejora_propuesta= pd.DataFrame(mejora_propuesta)
print(mejora_propuesta)
variacion_costos_por_arco = pd.DataFrame(variacion_costos_por_arco)
