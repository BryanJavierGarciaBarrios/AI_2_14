import ltl

# Definición de variables proposicionales
variables = {
    'A': ltl.Atom('A'),
    'B': ltl.Atom('B'),
    'C': ltl.Atom('C')
}

# Crear fórmulas
formula1 = ltl.AP('A') & ltl.AP('B')  # A y B son verdaderas simultáneamente
formula2 = ltl.G(ltl.AP('A') >> ltl.AP('B'))  # Siempre que A sea verdadero, B también debe ser verdadero
formula3 = ltl.X(ltl.AP('A') & ltl.AP('B'))  # En algún momento en el futuro, A y B serán verdaderos simultáneamente
formula4 = ltl.F(ltl.AP('A') | ltl.AP('B'))  # En algún momento en el futuro, A o B será verdadero

# Evaluar las fórmulas en un modelo
model = {
    0: {variables['A']: False, variables['B']: True, variables['C']: False},
    1: {variables['A']: True, variables['B']: True, variables['C']: False},
    2: {variables['A']: True, variables['B']: True, variables['C']: True}
}

# Evaluar las fórmulas en el modelo
print(f"El modelo satisface formula1: {ltl.formula(model, formula1)}")
print(f"El modelo satisface formula2: {ltl.formula(model, formula2)}")
print(f"El modelo satisface formula3: {ltl.formula(model, formula3)}")
print(f"El modelo satisface formula4: {ltl.formula(model, formula4)}")
