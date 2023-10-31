import clips

# Inicializar el entorno Clips
env = clips.Environment()

# Definir una función para crear un valor fuzzy
def define_fuzzy_value(env, name, value):
    env.build("(defglobal ?*fuzzy-value* = (create$ {0}))".format(name))
    env.build("(deffacts initial-fact (fact (name {0}) (value ?*fuzzy-value*)))".format(name))

# Definir un valor fuzzy "temperatura" con 3 términos lingüísticos
define_fuzzy_value(env, "temperatura", "[[frio 0 10] [templado 5 25] [caliente 20 30]]")

# Cargar reglas difusas
env.build('''
(defrule evaluar-temperatura
  ?f <- (fact (name temperatura) (value ?t))
  =>
  (printout t "Temperatura es " ?t crlf)
)
''')

# Evaluar una temperatura difusa
env.reset()
env.assert_string('(assert (name temperatura) (value [frio 5]))')
env.run()

env.reset()
env.assert_string('(assert (name temperatura) (value [templado 15]))')
env.run()

env.reset()
env.assert_string('(assert (name temperatura) (value [caliente 25]))')
env.run()
