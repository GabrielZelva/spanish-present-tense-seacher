# Spanish Present Tense Searcher
This is a program designed to scan a document in .txt format and find all fo the sentences which contain a present tense in Spanish.
It was developed to speed up sociolinguistic research related to morphology and syntax. 

## How to use it?

- Click [here](https://swlbj4-gabriel-p0.shinyapps.io/spanish_present_tense_searcher/) to access the program. 
- Select the text type. (NORMAL for standard raw text; PRESEEA for PRESEEA codified interviews)
- Upload a file in .txt format 

You can try with example.txt included in this repository, which is just a copy-pasted text from the [Spanish Wikipedia article on Sociolinguistics](https://es.wikipedia.org/wiki/Socioling%C3%BC%C3%ADstica).

## How does it work on the inside?

The program works in two stages:
First, an HMM tagger trained on the [AnCora corpus](https://github.com/UniversalDependencies/UD_Spanish-AnCora/tree/master) tags the sentences using the [Universal Dependencies](https://universaldependencies.org) PoS tags. It achieves 94.74% overall accuracy and f1 score for the VERB tag of 0.9185. 
In the second stage, a complex regex pattern (below) is used to separate present tenses from all the other tenses.
The sentences determined to contain at least one present tense are then saved and printed. 

The regex pattern: `[a-záéíóúñA-ZÁÉÍÓÚÑ]+((?<!(ad)|(id)|(and))o|(?<!(ab)|(í)|(ar))as|(?<!(ab)|(í)|(ar))a|(?<!(ab)|(í)|(ár))amos|áis|(?<!(ab)|(í)|(ar))an|[^s]es|[^s]e|[^rs]emos|[^r]éis|[^s]en|imos|ís|y){1}$`
  

## Some other linguistics research programs I have publicly available:

- [Praat script for advanced acoustic analysis of vowels](https://github.com/GabrielZelva/Praat-Advanced-Vowel-Analysis)
    - Takes in an audio recording and a segmentation, returns a tidy csv file with all the vowels analysed.
    - Users may customise the analysis to a really advanced degree.  
    
- [Spanish Future Tense Searcher](https://swlbj4-gabriel-p0.shinyapps.io/Buscador_de_futuros_interactivo/)
    - Works in the same way as this program, just for the future tenses. 
