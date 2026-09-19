from __future__ import annotations
from dataclasses import dataclass
from typing import Iterable

STATUSES = {
    "KILLED",
    "REDUCED_TO_KNOWN",
    "SURVIVES_CURRENT_TESTS",
    "EMPIRICALLY_SUPPORTED",
    "THEOREM_PROVED",
}

@dataclass(frozen=True)
class ClaimAudit:
    precise: bool
    counterexample_search: bool
    prior_art_attack: bool
    executable_model: bool
    randomized_tests: bool
    android_consequence: bool
    second_domain_consequence: bool
    explicit_falsifier: bool

def gate(a: ClaimAudit) -> str:
    checks = [
        a.precise,
        a.counterexample_search,
        a.prior_art_attack,
        a.executable_model,
        a.randomized_tests,
        a.android_consequence,
        a.second_domain_consequence,
        a.explicit_falsifier,
    ]
    if all(checks):
        return "SURVIVES_CURRENT_TESTS"
    return "UNRESOLVED"

def can_call_breakthrough(statuses: Iterable[str]) -> bool:
    s = set(statuses)
    # Deliberately conservative: software alone cannot certify novelty.
    return "THEOREM_PROVED" in s and "EMPIRICALLY_SUPPORTED" in s
