import os 
from Uzi_configuration import *

t = os.path.join(control, "Uzi_Collector.py")

os.system(f'start cmd /k python -u "{t}"')