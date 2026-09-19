from __future__ import annotations
import json
import sys
from dataclasses import dataclass
from pathlib import Path

@dataclass
class Observation:
    hypothesis_id: str
    reacquire_target: str
    exercise_old: str
    sensitive_effect: bool
    synthetic_only: bool = True

def classify(o: Observation) -> str:
    if not o.synthetic_only:
        return "INVALID_TEST"
    if o.reacquire_target == "denied" and o.exercise_old == "succeeded" and o.sensitive_effect:
        return "CANDIDATE_TEMPORAL_AUTHORITY_GAP"
    if o.exercise_old == "denied":
        return "INVARIANT_HOLDS_FOR_OBSERVATION"
    return "INCONCLUSIVE"

def main(path: str) -> None:
    raw = json.loads(Path(path).read_text())
    obs = Observation(**raw)
    print(json.dumps({
        "hypothesis_id": obs.hypothesis_id,
        "classification": classify(obs)
    }, indent=2))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: python lab/evaluate.py observation.json")
    main(sys.argv[1])
