from lab.convergence import (
    World,
    decision_incompatible_class,
    decision_neutral_admissible,
    separates_decisions,
    safe_separating_probe,
    unresolved_authority_obstruction,
)

def test_safe_separator_exists():
    worlds = [
        World("w0", "deny", (), frozenset({"inspect"})),
        World("w1", "allow", (), frozenset({"inspect"})),
    ]
    assert decision_incompatible_class(worlds)
    assert decision_neutral_admissible(worlds, "inspect")
    assert separates_decisions(worlds, ["red", "blue"])
    assert safe_separating_probe(worlds, "inspect", ["red", "blue"])
    assert not unresolved_authority_obstruction(worlds, {"inspect": ["red", "blue"]})

def test_authority_obstruction_when_probe_presupposes_disputed_decision():
    worlds = [
        World("w0", "deny", (), frozenset()),
        World("w1", "allow", (), frozenset({"execute"})),
    ]
    assert not decision_neutral_admissible(worlds, "execute")
    assert unresolved_authority_obstruction(worlds, {"execute": ["fail", "ok"]})

def test_nonseparating_probe_does_not_resolve():
    worlds = [
        World("w0", "deny", (), frozenset({"inspect"})),
        World("w1", "allow", (), frozenset({"inspect"})),
    ]
    assert not separates_decisions(worlds, ["same", "same"])
    assert unresolved_authority_obstruction(worlds, {"inspect": ["same", "same"]})
