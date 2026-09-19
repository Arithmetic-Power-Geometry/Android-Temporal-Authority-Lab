from lab.evidence import EvidenceRecord, digest, validate
import pytest

def record():
    return EvidenceRecord("TAC-001","Android","synthetic-build","emulator",
        "unlocked","locked","denied","succeeded",True,True,3,"synthetic fixture")

def test_evidence_digest_is_stable():
    assert digest(record()) == digest(record())

def test_real_user_data_is_rejected():
    r=EvidenceRecord("TAC-001","Android","x","emulator","a","b","denied","succeeded",True,False,1)
    with pytest.raises(ValueError):
        validate(r)
