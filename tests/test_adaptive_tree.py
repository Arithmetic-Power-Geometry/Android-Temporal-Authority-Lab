from lab.convergence import World, unresolved_authority_obstruction

def test_adaptive_tree_resolves_when_no_single_root_probe_finishes():
    worlds=[
      World("w0","deny",(),frozenset({"root","left"})),
      World("w1","allow",(),frozenset({"root","left"})),
      World("w2","deny",(),frozenset({"root","right"})),
      World("w3","allow",(),frozenset({"root","right"})),
    ]
    probes={
      "root":["L","L","R","R"],
      "left":["0","1","x","x"],
      "right":["x","x","0","1"],
    }
    assert not unresolved_authority_obstruction(worlds,probes)
