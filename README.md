# mgsub 

***A safe, multiple, simultaneous string substitution function***

## Why do I want this?
You have a string you want to make substitutions on. You want to make many different substitutions at the same time 
and you want them done in a safe way. For example, you want to shift each word in "hey, how are you?" to the left 
by replacing "hey" with "how", "how" with "are, etc.  This is a lightweight, pure python function with no 
dependencies to avoid package bloat when being used.

## Install it!

You need to have git installed

1. Clone the repo to your loacl machine. Type this in a command promp/terminal

```sh
git clone https://github.com/bmewing/mgsub-python
```

2. goto repo directory

```sh
cd mgsub-python
```

3. install the module

```sh
python setup.py install
```

4. You are all done!

## Usage

Simply pass in a vector of strings to be modified, a vector of patterns to match and a vector of replacements. Then watch as they are safely, simultaneously replaced!

```python
from mgsub import mgsub
mgsub(string, pattern=[], replacement=[], flags=0)
```

The pattern to match is supplied first and the replacement vector follows.

```python
mgsub("hey, how are you?",["hey","how","are","you"],["how","are","you","hey"])
```

Matches and replacements can still be supplied as regex exressions. Flags from `re` can be set to modify how the regex works.

```python
import re
mgsub("Dopazamine is not the same as Dopachloride and is still fake.", 
      [r'[Dd]opa(.*?mine)',"fake"], ["Meta\\1","real"], flags=re.I)
```