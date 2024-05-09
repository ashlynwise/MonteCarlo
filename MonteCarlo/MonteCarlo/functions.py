"""Provide the primary functions."""


def get_IsingHamiltonian(G, mus=None):
    if mus == None:
        mus = np.zeros(len(G.nodes()))

    if len(G.nodes()) != len(mus):
        error("DimensionMismatch")

    if len(G.nodes()) != len(mus):
        error(" Dimension Mismatch")
    J = [[] for i in G.nodes()]
    for e in G.edges:
        J[e[0]].append((e[1], G.edges[e]['weight']))
        J[e[1]].append((e[0], G.edges[e]['weight']))
    return montecarlo.IsingHamiltonian(J,mus)

if __name__ == "__main__":
    # Do something if this file is invoked on its own
    print(canvas())
