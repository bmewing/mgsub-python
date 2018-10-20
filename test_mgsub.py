import pytest
from mgsub import mgsub
import re

testdata = [
    ("hey, ho", ["hey", "ho"], ["ho", "hey"], 0, "ho, hey"),
    ("Production Workers, All Other", ["s$", "s([\.\, ]]", ",? All Other$"], ["", "\\1", ""], 0, "Production Workers"),
    ("Dopazamine and dopaloramide are fake chemicals.", ["dopa", "fake"], ["meta", "real"], re.I, "metazamine and metaloramide are real chemicals."),
    ("Hey, ho", ["hey"], ["tomorrow"], re.I, "tomorrow, ho"),
    ("Dopazamine and dopaloramide are fake chemicals.", ["dopa", "fake"], ["meta", "real"], re.I, "metazamine and metaloramide are real chemicals."),
    (["string", "test"], ["t"], ["p"], 0, ["spring", "pesp"]),
    (["Dopazamine is not the same as Dopachloride and is still fake.","dopazamine is undergoing a review by the fake news arm of the Dopazamine government"], ["[Dd]opa(.*?mine)", "fake"],["Meta\\1", "real"], 0, ["Metazamine is not the same as Dopachloride and is still real.", "Metazamine is undergoing a review by the real news arm of the Metazamine government"]),
    ("hey, ho", ["hey", "ho"], "yo", 0, "yo, yo"),
    (["hi there", "who said hi to me?", "who said hi"], ["^hi"], ["bye"], 0, ["bye there", "who said hi to me?", "who said hi"]),
    (["hi there", "who said hi to me?", "who said hi"], ["hi$"], ["bye"], 0, ["hi there", "who said hi to me?", "who said bye"]),
    ("ho ho hoot", ["h", "o"], ["o", "h"], 0, "oh oh ohht"),
    ("developer", ["e", "p"], ["p", "e"], 0, "dpvploepr"),
    ("hey, ho", ["hey", "ho"], ["ho", "hey"], 0, "ho, hey"),
    ("hi there, buddy boy!", ["there", "buddy"], ["where", "enemy"], 0, "hi where, enemy boy!"),
    ("they don't understand the value of what they seek.", ["the", "they"], ["a", "we"], 0, "we don't understand a value of what we seek."),
    ("hey, how are you?", ["hey", "how", "are", "you"], ["how", "are", "you", "hey"], 0, "how, are you hey?"),
    ("Dopazamine (of dopazamines family) is not the same as Dopachloride and is still fake.", ["[Dd]opa", "fake"], ["Meta", "real"], 0, "Metazamine (of Metazamines family) is not the same as Metachloride and is still real."),
    ("Dopazamine is not the same as Dopachloride and is still fake.", ["[Dd]opa(.*?mine)", "fake"], ["Meta\\1", "real"], 0, "Metazamine is not the same as Dopachloride and is still real."),
    ("Dopazamine and dopaloramide are fake chemicals.", ["dopa", "fake"], ["meta", "real"], re.I, "metazamine and metaloramide are real chemicals."),
    ("Dopazamine is a fake chemical", ["do.*ne", "dopazamin"], ["metazamine", "freakout"], re.I, "metazamine is a fake chemical"),
    ("hi there", ["why", "not", "go"], ["a", "b", "c"], 0, "hi there"),
    ("hi there", ["hi", "bye"], ["bye", "hi"], 0, "bye there"),
    ("the the the", ["the", "th"], ["a", "b"], 0, "a a a")
]

# (["string", None, "test"], ["t"], ["p"], 0, ["spring", None, "pesp"]),
# ([None, None, None, None], ["A"], ["b"], 0, [None, None, None, None]),
# (None, ["A"], ["b"], 0, None),


@pytest.mark.parametrize("s,p,r,f,expected", testdata)
def test_mgsub(s, p, r, f, expected):
    result = mgsub(s, p, r, f)
    assert expected == result
