from itertools import product,combinations
from lab.antichain_solver import Probe,root_resolvable,downward_closure_check
from lab.authority_fixedpoint import root_resolvable as fp_root, Probe as FP

def census(n=3):
    d=tuple("deny" if i%2==0 else "allow" for i in range(n))
    universe=[]
    for out in product("01",repeat=n):
      for adm in product((False,True),repeat=n):
        universe.append(Probe("p",out,adm))
    checked=0
    # exhaustive one-probe equivalence; selected two-probe combinations for n=3
    for p in universe:
      assert root_resolvable(d,[p])==fp_root(d,[FP(p.name,p.outcomes,p.admissible)])
      assert downward_closure_check(d,[p]);checked+=1
    for a,b in list(combinations(universe,2))[:2000]:
      ps=[a,b]; fps=[FP(x.name,x.outcomes,x.admissible) for x in ps]
      assert root_resolvable(d,ps)==fp_root(d,fps);checked+=1
    return {"n":n,"models_checked":checked,"status":"equivalent_on_census"}

if __name__=="__main__":print(census())
