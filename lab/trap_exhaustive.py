from itertools import product,combinations
from lab.authority_fixedpoint import Probe
from lab.trap_certificate import *

def census(n=3):
    d=tuple("deny" if i%2==0 else "allow" for i in range(n))
    universe=[]
    for out in product("01",repeat=n):
      for adm in product((False,True),repeat=n):
        universe.append(Probe(str(len(universe)),out,adm))
    checked=certs=0
    for p in universe:
      ps=[p]
      for C in deadsets(d,ps):
        w=trap_witness(C,d,ps)
        assert w is not None and verify_trap(C,w,d,ps)
        certs+=1
      checked+=1
    for a,b in list(combinations(universe,2))[:1000]:
      ps=[a,b]
      for C in deadsets(d,ps):
        w=trap_witness(C,d,ps)
        assert w is not None and verify_trap(C,w,d,ps)
        certs+=1
      checked+=1
    return {"models":checked,"verified_deadlock_certificates":certs}

if __name__=="__main__":print(census())
