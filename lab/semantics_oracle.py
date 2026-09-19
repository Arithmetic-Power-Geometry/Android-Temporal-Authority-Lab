"""Defensive oracle for classifying temporal-authority observations.

This module contains no exploit logic. It compares synthetic observations against
an explicitly declared expected lifetime policy.
"""
from dataclasses import dataclass
from enum import Enum

class Lifetime(str,Enum):
    ACTIVITY="activity"
    EXPLICIT_REVOCATION="explicit_revocation"
    PROFILE_AVAILABLE="profile_available"
    CREATOR_DEFINED="creator_defined"

@dataclass(frozen=True)
class Contract:
    capability:str
    lifetime:Lifetime
    expected_after_transition:bool
    source_note:str

@dataclass(frozen=True)
class Observation:
    acquired_before:bool
    fresh_after:bool
    old_after:bool
    sensitive_effect:bool
    synthetic_only:bool=True

def classify(c:Contract,o:Observation)->str:
    if not o.synthetic_only:return "INVALID_NON_SYNTHETIC"
    if not o.acquired_before:return "INVALID_NO_PRESTATE_CAPABILITY"
    if o.old_after==c.expected_after_transition:return "DOCUMENTED_OR_EXPECTED"
    if o.old_after and not c.expected_after_transition and o.sensitive_effect:
        return "SEMANTIC_MISMATCH_CANDIDATE"
    if not o.old_after and c.expected_after_transition:
        return "EARLY_INVALIDATION_OR_STRONGER_POLICY"
    return "INCONCLUSIVE"

def differential(o:Observation)->bool:
    """Fresh authority denied after transition while old authority still works."""
    return (not o.fresh_after) and o.old_after and o.sensitive_effect
