from itertools import product
from lab.authority_fixedpoint import Probe,root_resolvable,authority_deadlock_kernel

def census(n=3):
    decisions=tuple("deny" if i%2==0 else "allow" for i in range(n))
    probes=[]
    for out in product("01",repeat=n):
      for adm in product((False,True),repeat=n):
        probes.append(Probe(str((out,adm)),out,adm))
    dead=resolved=0
    for p in probes:
      if root_resolvable(decisions,[p]): resolved+=1
      else: dead+=1
    return {"n":n,"single_probe_models":len(probes),"resolved":resolved,"deadlocked":dead}

if __name__=="__main__": print(census())
