import re
import collections
from operator import itemgetter


def mgsub(string, pattern, replacement, flags=0):
    """Safe, multiple, simultaneous string substitution
    A safe, simultaneous, multiple global string replacement wrapper that allows access to multiple methods of
    specifying matches and replacements.
    :param string: list of strings where replacements are sought
    :param pattern: list of regular expressions to be matched
    :param replacement: list of regular expression replacements of either equal length to pattern (or a string to be
    recycled) which are a replacement for matched pattern
    :param flags: flags to be passed to re functions
    :return: return modified version of value(s) provided in string
    """

    assert isinstance(pattern, list), "Input pattern must be a list"
    assert ((isinstance(replacement, list) & (replacement.__len__() == pattern.__len__())) |
            isinstance(replacement, str)), "Input replacement must be a list of equal length to pattern or a string"

    if isinstance(replacement, str):
        replacement = [replacement for p in pattern]

    if not isinstance(string, str) and isinstance(string, collections.Sequence):
        output = [worker(s, pattern, replacement, flags) for s in string]
    else:
        output = worker(string, pattern, replacement, flags)
    return output


def worker(string, pattern, replacement, f):
    """ worker function
        The function that operates on a single string to do the work of mgsub
        :param string: string to be modified
        :param pattern: list of regular expressions to be matched
        :param replacement: list of regular expression replacements of either equal length to pattern (or a string to be
        recycled) which are a replacement for matched pattern
        :param f: flags to be passed to re functions
        :return: return modified version of string
    """
    matches = []
    for i in range(pattern.__len__()):
        matches.extend(gregexpr(pattern[i], string, i, f))
    matches.sort(key=itemgetter(2), reverse=True)
    for i in range(matches.__len__()-1, -1, -1):
        if any([filter_matches(matches[i], m) for m in matches[:i]]):
            matches.pop(i)
    matches.sort(key=itemgetter(1))
    for i in range(matches.__len__()-1, -1, -1):
        s = matches[i][1]
        e = matches[i][3]
        p = pattern[matches[i][0]]
        r = replacement[matches[i][0]]
        pre = string[:s]
        r0 = re.sub(p, r, string[s:e], flags=f)
        end = string[e:]
        string = pre+r0+end
    return string


def gregexpr(pattern, string, i, f):
    """ generate matrix of matches
        Find all instances of a given pattern in a string and return a 2d array with key info
        :param pattern: pattern to be matched
        :param string: string to be modifed
        :param i: index of the pattern being provided
        :param f: flags to be passed to re functions
        :return: 2d array with values for index of pattern, start of a match, length of match and end of match
    """
    greg = re.finditer(pattern, string, flags=f)
    output = [[i, r.start(), r.group().__len__()] for r in greg]
    for o in output:
        o.append(o[1]+o[2])
    return output


def filter_matches(this, prev):
    """ filter match array
        Logic to determine if a match is overlapped by another match
        :param this: the match currently be checked
        :param prev: an earlier (longer) match currently being compared against
        :return boolean indicating overlap
    """
    s = this[1]
    e = this[3]
    ps = prev[1]
    pe = prev[3]
    return ((ps <= s) & (pe > s)) | ((ps < e) & (pe >= e))
