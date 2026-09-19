"""Authorization-aware comparison of experiments.

Core distinction:
- raw informativeness: which decision distinctions a probe can reveal;
- safe informativeness: those distinctions only where the probe is jointly admissible.

This module searches for reversals where a raw-more-informative probe is unusable
for the decision while a raw-less-informative probe safely resolves it.
"""
from dataclasses import dataclass
from itertools import product

@dataclass(frozen=True)
class Experiment:
    name: str
    outcomes: tuple[str,...]
    admissible: tuple[bool,...]

def partition(exp:Experiment):
    b={}
    for i,o in enumerate(exp.outcomes): b.setdefault(o,set()).add(i)
    return tuple(sorted((tuple(sorted(v)) for v in b.values())))

def refines(a:Experiment,b:Experiment)->bool:
    """Every a-cell lies inside a b-cell: a is at least as informative as b."""
    pa=partition(a); pb=partition(b)
    return all(any(set(x)<=set(y) for y in pb) for x in pa)

def universally_admissible(e:Experiment, live:tuple[int,...])->bool:
    return all(e.admissible[i] for i in live)

def resolves(e:Experiment, decisions:tuple[str,...], live=None)->bool:
    live=live or tuple(range(len(decisions)))
    if not universally_admissible(e,live): return False
    buckets={}
    for i in live: buckets.setdefault(e.outcomes[i],set()).add(decisions[i])
    return all(len(v)==1 for v in buckets.values())

def authority_information_reversal(stronger:Experiment,weaker:Experiment,decisions):
    """Raw stronger experiment loses to weaker experiment after admissibility."""
    return (refines(stronger,weaker) and
            not resolves(stronger,decisions) and
            resolves(weaker,decisions))

def enumerate_reversals(n=3):
    decisions=tuple("deny" if i%2==0 else "allow" for i in range(n))
    exps=[]
    for outs in product(("0","1"),repeat=n):
      for adm in product((False,True),repeat=n):
        exps.append(Experiment("e",outs,adm))
    hits=[]
    for a in exps:
      for b in exps:
        if authority_information_reversal(a,b,decisions):
          hits.append((a,b))
    return hits

if __name__=="__main__":
    h=enumerate_reversals(3)
    print({"three_world_authority_information_reversals":len(h)})
    if h: print(h[0])
