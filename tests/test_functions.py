from universal_profanity.profanity import UniversalProfanity


def test_censor():
    # Censor some text
    profanity = UniversalProfanity(country='en', replace_chars='*')
    text = 'Oh shit I saw some bitch scraping my car!'
    assert profanity.censor(text) == 'Oh **** I saw some ***** scraping my car!'


def test_censor_multilanguage():
    # Censor some text in multimple languages
    profanity = UniversalProfanity(country=['en', 'ru'], replace_chars='*')
    text = 'Бля я fuck that shit'
    assert profanity.censor(text) == '*** я **** that ****'


def test_contains_profanity():
    # Check if text contains profanity words
    profanity = UniversalProfanity(country='en', replace_chars='*')
    text = 'I fucked this up'
    assert profanity.contains_profanity(text) is True
