import inspect
import sys

f = inspect.currentframe()
local_variables = f.f_locals
global_variables = f.f_globals

a = 5
print(local_variables)
a = 6
print(local_variables)

