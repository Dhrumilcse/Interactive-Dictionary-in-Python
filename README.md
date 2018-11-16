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
> Load the data, and just check if data loaded correctly.

```
dictionary_2.py
```
> Check for non-existing words.

```
dictionary_3.py
```
> Removing the case-sensitivity from the program. For example 'Rain' and 'rain' will give same output.

```
dictionary_4-1.py
dictionary_4-2.py
```
> Learn how to 'difflib' works in order to suggest a similar word.

```
dictionary_5.py
```
> Use 'difflib' in our code to retrieve closest match

```
dictionary_6.py
```
> If the suggested word is what user wants, retrive the meaning of suggested word.

```
dictionary_7.py
```
> If the word has more than 1 definition, retrive all by iterating.

Note: All files are integrated with comments to help you understand each and every line/command of the code.

### Run All Together
Even though the dictionary_7.py is the complete file, I made a new copy of that file namely interactive_dictionary.py to serve as a final file.
```
python3 interactive_dictionary.py
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details
