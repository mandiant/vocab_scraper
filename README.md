# Vocabulary Scraper

Vocabulary Scraper is meant to aid analysis of foreign-language codebases. It
reads source files (`*.{c,h,cpp,hpp,txt}`) and writes a prioritized vocabularly
list in UTF-8. It was written and used by FLARE to [analyze the Carbanak source
code](https://www.fireeye.com/blog/threat-research/2019/04/carbanak-week-part-one-a-rare-occurrence),
and accordingly, the default setting is to read files in code page 1251
(Cyrillic).

## Usage

Vocabulary Scraper accepts the following arguments:

```
usage: vocab.py [-h] [--startdir STARTDIR] [--ienc IENC] [--oenc OENC] outfile

Vocabulary scraper

positional arguments:
  outfile              Output file

optional arguments:
  -h, --help           show this help message and exit
  --startdir STARTDIR  Directory to recurse
  --ienc IENC          Input encoding
  --oenc OENC          Output encoding
```

The default input encoding is `cp1251` and the default output encoding is
`utf-8`. Any character encoding name recognized by the Python standard
libraries should work.

## Limitations relating to Linguistic Concerns
Vocabulary Scraper is best for languages like Russian where words are
conveniently delimited by spaces. In languages where spaces are not mandated
between words (like Chinese and Japanese), Vocabulary Scraper might still
extract all the foreign language text, however it will not be able to break the
symbol sequences out into individual vocabulary words to study if there are no
spaces.

Vocabulary Scraper does not aggregate or coalesce entries with common word
roots due to plural, different verb conjugations, etc. In a sufficiently large
corpus, it may help to groom the list manually to coalesce like terms.

## Limitations relating to Character Encoding
Vocabulary Scraper currently does not coalesce words having alternate encodings
of the same character(s), meaning it could produce a list containing one or
more sets of words are visually identical but are counted as distinct based on
their differing Unicode code points. This has not yet been observed in
operation, but if you observe this, this might explain the cause.

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
