from __future__ import annotations
from dataclasses import dataclass, asdict
from hashlib import sha256
import json
from pathlib import Path
from typing import Any, Dict

@dataclass(frozen=True)
class EvidenceRecord:
    hypothesis_id: str
    platform: str
    build: str
    device_class: str
    acquire_state: str
    target_state: str
    reacquire_result: str
    old_capability_result: str
    sensitive_effect: bool
    synthetic_only: bool
    repetitions: int
    notes: str = ""

def validate(r: EvidenceRecord) -> None:
    if not r.synthetic_only:
        raise ValueError("lab accepts synthetic/owned test data only")
    if r.repetitions < 1:
        raise ValueError("repetitions must be >= 1")
    if r.reacquire_result not in {"allowed","denied","not_tested"}:
        raise ValueError("invalid reacquire_result")
    if r.old_capability_result not in {"succeeded","denied","not_tested"}:
        raise ValueError("invalid old_capability_result")

def canonical(r: EvidenceRecord) -> str:
    validate(r)
    return json.dumps(asdict(r), sort_keys=True, separators=(",",":"))

def digest(r: EvidenceRecord) -> str:
    return sha256(canonical(r).encode()).hexdigest()

def write_record(r: EvidenceRecord, path: str) -> Dict[str,Any]:
    body={"record":asdict(r),"sha256":digest(r)}
    Path(path).write_text(json.dumps(body,indent=2,sort_keys=True)+"\n")
    return body
