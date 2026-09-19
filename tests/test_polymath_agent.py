from lab.polymath_agent import World,Probe,Problem,safe_separable,obstruction_kernel,lens_report
from lab.exhaustive_search import search_two_world_binary

def test_safe_probe_resolves():
    p=Problem(
      (World("a","deny"),World("b","allow")),
      (Probe("public",frozenset({"a","b"}),(("a","0"),("b","1"))),))
    assert safe_separable(p)
    assert obstruction_kernel(p)==[]

def test_disputed_probe_creates_obstruction():
    p=Problem(
      (World("a","deny"),World("b","allow")),
      (Probe("needs_allow",frozenset({"b"}),(("a","0"),("b","1"))),))
    assert not safe_separable(p)
    assert obstruction_kernel(p)==[("a","b")]
    assert lens_report(p)["authorization_safe_separable"] is False

def test_exhaustive_search_finds_informative_but_unsafe_cases():
    s=search_two_world_binary()
    assert len(s)>0
    # all survivors are observationally informative yet not safely usable
    assert all(obs[0]!=obs[1] for _,obs,_ in s)
