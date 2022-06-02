# easyReading
This project implements a semi-automatic mechanism created to simplify periphrasis on a text based on Easy Reading Methodology.
This project belongs to a End-of-Degree Project developed by Julia Antona Palacios.
## Requeriments ##
* Python 3.9

https://www.python.org/downloads/release/python-390/

* Spacy
```python
pip install -U spacy
python -m spacy download es_core_news_lg
```
* SpellChecker
```python
pip install pyspellchecker
```
* Mlconjug
```python
pip install mlconjug
```
* Flask
```python
pip install Flask
```
## Project Organitation ##
- server.py: python server with simplification service
* templates 
  - index.html: HTML file with UI styles and and logic
 * modules/utils
    * contextAdder
        - context.py: add context to certain periphrasis 
        - dataContext.py: saves the type of the periphrasis and their correspondatn context
    * simplifier
        - classifier.py: classifies periphrasis
        - conjugator.py: conjugates root verb with auxiliar verb morphology
        - dictionary.py: checks grammar of a certain word
        - grammaticalData.py: saves grammatical information such as periphrasis classification
        - processor.py: process and creates a dictionary with all the information of a certain periphrasis
        - pronounFixer.py: corrects and associates reflexive pronouns to its resperctive verb
      
    * tests: contains test corpus
    periphrasisSimplifier.py: princial module, recieves an input text and a list of periphrasis and uses all the other modules to simplify it.
    
## Use ##
To use the simplification service just run
```python
python .\server.py 
```
