
from pgmpy.models import DynamicBayesianNetwork as DBN
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import DBNInference

# Definir la estructura de la DBN
dbn = DBN()

# Definir los nodos y las conexiones temporales
dbn.add_edges_from([(('X', 0), ('X', 1)), (('X', 1), ('X', 2))])

# Definir las distribuciones condicionales temporales
cpd_x0 = TabularCPD(('X', 0), 2, [[0.6], [0.4]])
cpd_x1 = TabularCPD(('X', 1), 2, [[0.3, 0.7], [0.7, 0.3]], evidence=[('X', 0)], evidence_card=[2])
cpd_x2 = TabularCPD(('X', 2), 2, [[0.2, 0.8], [0.8, 0.2]], evidence=[('X', 1)], evidence_card=[2])

# Agregar las distribuciones condicionales temporales a la DBN
dbn.add_cpds(cpd_x0, cpd_x1, cpd_x2)

# Verificar si la DBN es válida
print("¿Es válida la DBN?", dbn.check_model())

# Realizar inferencia en la DBN
inference = DBNInference(dbn)
result = inference.query(variables=[('X', 2)], evidence={('X', 0): 1})
print("Probabilidad de X en el tiempo 2 dado X en el tiempo 0 igual a 1:", result)
