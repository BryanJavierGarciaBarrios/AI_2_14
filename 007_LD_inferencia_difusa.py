import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Crear variables difusas de entrada y salida
temperatura = ctrl.Antecedent(np.arange(0, 101, 1), 'temperatura')
humedad = ctrl.Antecedent(np.arange(0, 101, 1), 'humedad')
velocidad_ventilador = ctrl.Consequent(np.arange(0, 101, 1), 'velocidad_ventilador')

# Definir funciones de membresía para las variables difusas
temperatura['fria'] = fuzz.trimf(temperatura.universe, [0, 0, 50])
temperatura['calida'] = fuzz.trimf(temperatura.universe, [0, 50, 100])

humedad['seca'] = fuzz.trimf(humedad.universe, [0, 0, 50])
humedad['humeda'] = fuzz.trimf(humedad.universe, [0, 50, 100])

velocidad_ventilador['baja'] = fuzz.trimf(velocidad_ventilador.universe, [0, 0, 50])
velocidad_ventilador['alta'] = fuzz.trimf(velocidad_ventilador.universe, [0, 50, 100])

# Definir reglas difusas
regla1 = ctrl.Rule(temperatura['fria'] & humedad['seca'], velocidad_ventilador['alta'])
regla2 = ctrl.Rule(temperatura['calida'] & humedad['humeda'], velocidad_ventilador['baja'])

# Crear sistema de control difuso
sistema_ctrl = ctrl.ControlSystem([regla1, regla2])

# Simular el sistema de control con valores de entrada
sistema = ctrl.ControlSystemSimulation(sistema_ctrl)
sistema.input['temperatura'] = 30
sistema.input['humedad'] = 70

# Realizar la inferencia difusa
sistema.compute()

#
