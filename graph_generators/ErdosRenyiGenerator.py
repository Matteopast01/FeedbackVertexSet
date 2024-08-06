import networkit as nk

class ErdosRenyiGenerator:
    _number_nodes: int
    _p: float

    def __init__(self, number_nodes, p):
        self._number_nodes = number_nodes
        self._p = p

    def erdos_renyi_generator(self):
        generator = nk.generators.ErdosRenyiGenerator(self._number_nodes, self._p)
        G = generator.generate()
        return G
