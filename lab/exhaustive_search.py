"""Finite exhaustive search for the smallest unresolved-authority obstruction."""
from itertools import product
from lab.polymath_agent import World, Probe, Problem, safe_separable, obstruction_kernel

def search_two_world_binary():
    worlds=(World("w0","deny"),World("w1","allow"))
    survivors=[]
    # Each probe has admissibility mask over worlds and binary outcomes.
    for adm in product((0,1), repeat=2):
      allowed=frozenset(f"w{i}" for i,x in enumerate(adm) if x)
      for obs in product(("0","1"), repeat=2):
        e=Probe("e",allowed,(("w0",obs[0]),("w1",obs[1])))
        p=Problem(worlds,(e,))
        informative=obs[0]!=obs[1]
        if informative and not safe_separable(p):
          survivors.append((adm,obs,obstruction_kernel(p)))
    return survivors

if __name__=="__main__":
    s=search_two_world_binary()
    print("minimal_survivors",len(s))
    for x in s: print(x)
