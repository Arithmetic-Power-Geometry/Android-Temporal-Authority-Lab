from lab.model_search import enumerate_two_world_two_probe_models, summary

def test_exhaustive_search_finds_obstructions():
    xs=enumerate_two_world_two_probe_models()
    assert len(xs)>0
    assert summary()["minimal_obstructions"]==len(xs)

def test_every_returned_model_is_nontrivial():
    for x in enumerate_two_world_two_probe_models():
        assert x.decisions[0] != x.decisions[1]
