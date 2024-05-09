import numpy as np
import math             

class BitString:
    """
    Simple class to implement a config of bits
    """
    def __init__(self, N):
        self.N = N
        self.config = np.zeros(N, dtype=int)
    
    def __str__(self):
        return f"{self.config}"
    
    def __eq__(self, other):        
        for values in zip(self.config, other.config):
            if values[0] != values[1]:
                return False
        return True
        
    def __len__(self):
        counter = 0
        for _ in self.config:
            counter += 1
        return counter
    
    def on(self):
        counter = 0
        for value in self.config:
            if value == 1:
                counter += 1
        return counter
    
    def off(self):
        counter = 0
        for value in self.config:
            if value == 0:
                counter += 1
        return counter
    
    def flip_site(self,i):
        self.config[i] = int(not self.config[i])
    
    def int(self):
        int_value = int("".join([str(i) for i in self.config]), 2)
        return int_value
        
    def set_config(self, s:list[int]):
        self.config = s
    
    def set_int_config(self, dec:int):
        bin_value = str(bin(dec))[2::] 
        new_config = [value for value in bin_value]
        if len(new_config) != self.N:
            new_config = "".join(new_config)
            new_config = new_config.zfill(self.N)
        new_config = [int(value) for value in new_config]
        self.config = np.array(new_config)

def energy(bs: BitString, G: nx.Graph):
    """Compute energy of configuration, `bs`

        .. math::
            E = \\left<\\hat{H}\\right>

    Parameters
    ----------
    bs   : Bitstring
        input configuration
    G    : Graph
        input graph defining the Hamiltonian
    Returns
    -------
    energy  : float
        Energy of the input configuration
    """
    energy = 0
    for i in G.edges:
