# universal-profanity: A Python library for detecting and filtering profanity

## Overview
`universal-profanity` Universal Profanity is a versatile library designed for the detection and filtration of
profanity across a wide range of languages. The library cover 25 languages.

### Features
1. Full text or individual words censoring.
2. Multilingual support, including profanity filtering in texts written in mixed languages.
3. Partial word censoring.
4. There are 25 popular languages to work with.

## Usage
Here are the basic examples of how to use the library. For more examples please see `tests` folder.

### Basics
```python
from universal_profanity.profanity import UniversalProfanity

pf = UniversalProfanity()
pf.censor('Shit, I fucked up')
# !*@^, I $#%@!$ up

pf.contains_profanity('Fck dude')
# True
```

### More options
```python
from universal_profanity.profanity import UniversalProfanity

pf = UniversalProfanity(country='en', replace_chars='*')
pf.censor('Shit, that is bullshit!')
# ****, that is ********!

pf = UniversalProfanity(country=['en', 'ru'], replace_chars='*#')
pf.censor('Бля я fuck that shit')
# #** я #*## that **#*

```

### Customizations
```python
from universal_profanity.profanity import UniversalProfanity

pf = UniversalProfanity()

pf.set_censor_characters('$')
pf.censor("That's bullshit!")
# "That's $$$$$$$$!"
```

## Installation
First two parts of installation instructions are designed for the users who want to filter English profanity.
If you want to filter profanity in another language you still need to read it.

### Basic installation
You need to install `universal-profanity`:
```shell
$ pip install universal-profanity
```

## Available country codes
- **th** - Thai 🇹🇭
- **fr** - French 🇫🇷
- **uk** - Ukrainian 🇺🇦
- **gr** - Greek 🇬🇷
- **ge** - German 🇩🇪
- **cz** - Czech 🇨🇿
- **sp** - Spanish 🇪🇦
- **bu** - Bulgarian 🇧🇬
- **tc** - Tchinese 🇨🇳
- **da** - Danish 🇩🇰
- **po** - Polish 🇵🇱
- **en** - English 	🏴󠁧󠁢󠁥󠁮󠁧󠁿
- **br** - Brazilian 🇧🇷
- **du** - Dutch 🇳🇱
- **fi** - Finnish 🇫🇮
- **no** - Norwegian 🇳🇴
- **in** - Indonesian 🇮🇩
- **ja** - Japanese 🇯🇵
- **tu** - Turkish 🇹🇷
- **ru** - Russian 🇷🇺
- **ro** - Romanian 🇷🇴
- **sc** - Schinese 🇨🇳
- **it** - Italian 🇮🇹
- **ko** - Korean 🇰🇷
- **sw** - Swedish 🇸🇪
- **vi** - Vietnamese 🇻🇳
- **hu** - Hungarian 🇭🇺
- **la** - Latam

