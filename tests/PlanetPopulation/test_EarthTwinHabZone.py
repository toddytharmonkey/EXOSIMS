r"""Test code for EarthTwinHabZone modules within EXOSIMS PlanetPopulation.

Sonny Rappaport, Cornell, September 2021 

Original code written by: 
Cate Liu, IPAC, 2016
"""

import unittest
import EXOSIMS
from EXOSIMS import MissionSim
from EXOSIMS.Prototypes.PlanetPopulation import PlanetPopulation
import EXOSIMS.PlanetPopulation
from EXOSIMS.PlanetPopulation.EarthTwinHabZone1 import EarthTwinHabZone1
from EXOSIMS.util.get_module import get_module
import pkgutil, os, json, sys, copy
import numpy as np
from astropy import units as u
import scipy.stats


class TestEarthTwinHabZone(unittest.TestCase):
    
    def setUp(self):

        self.spec = {'modules':{'PlanetPhysicalModel': ''}}
        self.dev_null = open(os.devnull, 'w')
        self.allmods = [] 
        pkg = EXOSIMS.PlanetPopulation
        modtype = getattr(PlanetPopulation,'_modtype')
        for loader, module_name, is_pkg in pkgutil.walk_packages(pkg.__path__, pkg.__name__ + '.'):
            if 'EarthTwinHabZone' in module_name:
                mod = get_module(module_name.split('.')[-1], modtype)
                self.allmods.append(mod)

        print("\n\n\n")
        print(self.allmods)
        print("\n\n\n")
    
    def tearDown(self):
        pass
    
    def test_gen_plan_params(self):
        r"""Test generated planet parameters

        For every EarthTwinHabZone, undergoes a specialized test suite. Not the 
        most efficient right now.  
        """

        for mod in self.allmods:

            obj = mod(**copy.deepcopy(self.spec))

if __name__ == "__main__":
    unittest.main()
