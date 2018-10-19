import re
from operator import itemgetter


def mgsub(string, pattern=[], replacement=[]):
    if not isinstance(string, str):
        output = [worker(s, pattern, replacement) for s in string]
    else:
        output = worker(string, pattern, replacement)
    return output


def worker(string, pattern=[], replacement=[]):
    matches = []
    for i in range(pattern.__len__()):
        matches.extend(gregexpr(pattern[i], string, i))
    matches.sort(key=itemgetter(2), reverse=True)
    for i in range(matches.__len__()-1, -1, -1):
        if any([filter_matches(matches[i], m) for m in matches[:i]]):
            matches.pop(i)
    for i in range(matches.__len__()-1, -1, -1):
        s = matches[i][1]
        e = matches[i][3]
        p = pattern[matches[i][0]]
        r = replacement[matches[i][0]]
        pre = string[:s]
        r0 = re.sub(p,r,string[s:e])
        end = string[e:]
        string = pre+r0+end
    return string


def gregexpr(pattern, string, i):
    greg = re.finditer(pattern, string)
    output = [[i, r.start(), r.group().__len__()] for r in greg]
    for o in output:
        o.append(o[1]+o[2])
    return output


def filter_matches(this, prev):
    s = this[1]
    e = this[3]
    ps = prev[1]
    pe = prev[3]
    return ((ps <= s) & (pe >= s)) | ((ps <= e) & (pe >= e))
