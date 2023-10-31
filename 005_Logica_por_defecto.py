# Definición de un valor por defecto para un predicado
def default_predicate(p):
    return not p

# Regla de inferencia por defecto
def default_inference(rule, facts):
    head, body = rule

    if all(fact in facts or default_predicate(fact) for fact in body):
        facts.add(head)
        return True
    else:
        return False

# Ejemplo de reglas y hechos
rules = [(['A'], ['B', 'C']), (['D'], ['E']), (['F'], ['G', 'H'])]
facts = set(['B', 'E', 'H'])

# Realizar razonamiento de lógica por defecto
changed = True
while changed:
    changed = False
    for rule in rules:
        if default_inference(rule, facts):
            changed = True

# Resultado final
print("Hechos finales:", facts)
