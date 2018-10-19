# mgsub 

***A safe, multiple, simultaneous string substitution function***

## Why do I want this?
You have a string you want to make substitutions on. You want to make many different substitutions at the same time 
and you want them done in a safe way. For example, you want to shift each word in "hey, how are you?" to the left 
by replacing "hey" with "how", "how" with "are, etc.  This is a lightweight, pure python function with no 
dependencies to avoid package bloat when being used.

## Install it!

I'm still figuring this part out, not ready yet (sorry!)

## Usage

Simply pass in a vector of strings to be modified, a vector of patterns to match and a vector of replacements. Then watch as they are safely, simultaneously replaced!

```python
from mgsub import mgsub
mgsub(string,pattern=[],replacement=[])
```

The pattern to match is supplied first and the replacement vector follows.

```python
mgsub("hey, how are you?",["hey","how","are","you"],["how","are","you","hey"])
```

Matches and replacements can still be supplied as regex exressions. Additional arguments can be passed to the `sub`/`gsub`/`gregexpr` family of internal functions.

```python
mgsub("Dopazamine is not the same as Dopachloride and is still fake.", 
      [r'[Dd]opa(.*?mine)',"fake"], ["Meta\\1","real"])
```