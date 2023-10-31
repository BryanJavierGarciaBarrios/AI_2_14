#pip install modal-logic-parser

from modal_logic_parser import World, Atom, Box, K

# Definir mundos posibles
world1 = World('1')
world2 = World('2')
world3 = World('3')

# Definir átomos proposicionales
p = Atom('p')
q = Atom('q')
r = Atom('r')

# Establecer relaciones entre mundos
world1.relate(world2)
world2.relate(world3)

# Establecer fórmulas modales
formula1 = Box(p)
formula2 = Box(Box(q) | Box(r))
formula3 = K(p, q)

# Evaluar fórmulas en mundos específicos
print(f"En el mundo 1, p es {formula1.evaluate(world1)}")
print(f"En el mundo 1, Box(Box(q) | Box(r)) es {formula2.evaluate(world1)}")
print(f"En el mundo 1, K(p, q) es {formula3.evaluate(world1)}")

print(f"En el mundo 2, p es {formula1.evaluate(world2)}")
print(f"En el mundo 2, Box(Box(q) | Box(r)) es {formula2.evaluate(world2)}")
print(f"En el mundo 2, K(p, q) es {formula3.evaluate(world2)}")

print(f"En el mundo 3, p es {formula1.evaluate(world3)}")
print(f"En el mundo 3, Box(Box(q) | Box(r)) es {formula2.evaluate(world3)}")
print(f"En el mundo 3, K(p, q) es {formula3.evaluate(world3)}")
