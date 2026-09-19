"""Finite checker for safe-garbling restoration and its failure witness."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Exp:
    outcomes: tuple[str,...]
    admissible: tuple[bool,...]

def refines(a:Exp,b:Exp)->bool:
    for i in range(len(a.outcomes)):
      for j in range(len(a.outcomes)):
        if a.outcomes[i]==a.outcomes[j] and b.outcomes[i]!=b.outcomes[j]:
          return False
    return True

def admissibility_covers(a:Exp,b:Exp)->bool:
    """Where b can be acquired, a can also be acquired."""
    return all((not bb) or aa for aa,bb in zip(a.admissible,b.admissible))

def safe_garbling_restored(a:Exp,b:Exp)->bool:
    return refines(a,b) and admissibility_covers(a,b)

def witness_failure(a:Exp,b:Exp):
    if not refines(a,b): return None
    for i,(aa,bb) in enumerate(zip(a.admissible,b.admissible)):
      if bb and not aa:
        return {"world":i,"reason":"weaker experiment is acquirable but stronger source is not"}
    return None
