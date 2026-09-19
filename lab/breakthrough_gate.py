"""Evidence-based breakthrough gate. Passing unit tests is deliberately insufficient."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Evidence:
    exact_theorem: bool=False
    exhaustive_small_models: bool=False
    prior_art_reduction_survived: bool=False
    nontrivial_separation: bool=False
    empirical_new_failure_class: bool=False
    independent_replication: bool=False

def verdict(e:Evidence)->str:
    # Require prior-art survival plus either a nontrivial separation or empirical class,
    # and require formal/computational support. Independent replication is reserved
    # for the strongest label.
    core=e.exact_theorem and e.exhaustive_small_models and e.prior_art_reduction_survived
    contribution=e.nontrivial_separation or e.empirical_new_failure_class
    if core and contribution and e.independent_replication:
        return "BREAKTHROUGH_CANDIDATE_STOP_AND_WRITE"
    if core and contribution:
        return "STRONG_RESULT_NEEDS_INDEPENDENT_REPLICATION"
    return "NO_BREAKTHROUGH_CONTINUE"

CURRENT=Evidence(
 exact_theorem=True,
 exhaustive_small_models=True,
 prior_art_reduction_survived=False,
 nontrivial_separation=False,
 empirical_new_failure_class=False,
 independent_replication=False)

if __name__=="__main__": print(verdict(CURRENT))
