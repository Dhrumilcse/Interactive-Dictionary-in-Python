# Interactive Dictionary in Python
Create a dictionary in Python which can retrieve definitions for user, ask 'did you mean this instead?' if user made a typo while entering the word, and if the word has more than one definition then retrieve them all.

## 1. Installing dependencies

Installing dependencies is the first thing you want to do.
```
import json
import difflib
```

## 2. Understanding files in the directory

### Data
The data is in .json format and can be found as,
```
dictionary.json
```

### Step by Step Solution
``` 
dictionary_1.py
```
> Load the data, and just check is the data has loaded correctly.

```
dictionary_2.py
```
> Check for non-existing words.

```
dictionary_3.py
```
> Removing the case-sensitivity from the program. For example 'Rain' and 'rain' will give same output.
