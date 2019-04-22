# Vocabulary Scraper

Vocabulary Scraper is meant to aid analysis of foreign-language codebases. It
reads source files (`*.{c,h,cpp,hpp,txt}`) and writes a prioritized vocabularly
list in UTF-8. It was written and used by FLARE to analyze the Carbanak source
code, and accordingly, the default setting is to read files in code page 1251
(Cyrillic).

## Limitations relating to Different Languages
Vocabulary Scraper is best for languages like Russian where words are
conveniently delimited by spaces. In languages where spaces are not mandated
between words (like Chinese and Japanese), Vocabulary Scraper might still
extract all the foreign language text, however it will not be able to break the
symbol sequences out into individual vocabulary words to study if there are no
spaces.

## Limitations relating to Character Encoding
Vocabulary Scraper does not aggregate or coalesce entries with common word
roots due to plural, different verb conjugations, etc. In a sufficiently large
corpus, it may help to groom the list manually to coalesce like terms.

The script also currently does not coalesce words having alternate encodings of
the same character(s), meaning it could produce a list containing one or more
sets of words are visually identical but are counted as distinct based on their
differing Unicode code points. This has not yet been observed in operation, but
if you observe this, this might explain the cause.

As of this writing, Vocabulary Scraper is ignorant of the real encoding of its
input files (use the command line argument --ienc to specify the encoding,
default cp1251).  Heuristic-based sniffing of the character encoding is
possible via libraries like `chardet`.

This script is also ignorant of the erroneous "words" that can arise from
incorrectly assuming the character encoding. If you do not add any heuristic
character encoding detection, then you may need to observe results and adjust
by performing a survey of the files in your corpus and partitioning them
according to character encoding to run them in separate runs of this tool
(with different character encodings assumed), then merge and sort the text
numerically (and once again coalesce duplicates and near-duplicates).

The book "Fluent Python" has a whole chapter that treats Python character
encoding topics in great detail if you are looking for a reference.