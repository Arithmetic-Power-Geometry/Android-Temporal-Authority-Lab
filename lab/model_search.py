from __future__ import annotations
from dataclasses import dataclass
from itertools import product
from typing import Dict, List, Tuple
from lab.convergence import World, unresolved_authority_obstruction

@dataclass(frozen=True)
class MinimalObstruction:
    decisions: Tuple[str, ...]
    admissibility: Tuple[Tuple[bool, ...], ...]
    outcomes: Tuple[Tuple[int, ...], ...]

def enumerate_two_world_two_probe_models() -> List[MinimalObstruction]:
    """
    Exhaustively enumerate the smallest non-trivial binary decision/probe models.
    This is a theorem-discovery instrument, not an Android exploit generator.
    """
    found: List[MinimalObstruction] = []
    decisions=("deny","allow")
    for adm_bits in product([False,True], repeat=4):
        # rows=worlds, cols=probes
        adm=((adm_bits[0],adm_bits[1]),(adm_bits[2],adm_bits[3]))
        worlds=[
            World("w0", decisions[0], (), frozenset(p for p,j in zip(("p0","p1"),adm[0]) if j)),
            World("w1", decisions[1], (), frozenset(p for p,j in zip(("p0","p1"),adm[1]) if j)),
        ]
        for out_bits in product([0,1], repeat=4):
            outs=((out_bits[0],out_bits[1]),(out_bits[2],out_bits[3]))
            probes={"p0":[str(outs[0][0]),str(outs[1][0])],
                    "p1":[str(outs[0][1]),str(outs[1][1])]}
            if unresolved_authority_obstruction(worlds, probes):
                found.append(MinimalObstruction(decisions, adm, outs))
    return found

def summary() -> Dict[str,int]:
    models=enumerate_two_world_two_probe_models()
    return {"minimal_obstructions":len(models)}

if __name__=="__main__":
    print(summary())
