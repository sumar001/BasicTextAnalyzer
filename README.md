# Project: Text Analyzer
### Name: Saad Umar
### Course: INF 1340 - Programming for Data Science
### Lec0101 - Monday - 3pm to 6pm
### Instructor: Dr. Maher Elshakankiri

## Program Explanation
This project involves creating a text analyzer using python programming to analyze different text files and gain insights to the file. The program consists of 13 functions, two of them are to read and write the input and output files, while the remaining 11 functions perform different types of analysis on the input text file.
This program will prompt the user to enter the name of the input file which they wish to analyze. They will then be asked to write the name of the output file to which the results will be displayed. The output of this file will be displayed on the screen, as well as be saved in an output file. Additionally, the output of the termFrequency_idf and count_chars functions will be saved in a csv file as well as in the output file and displayed on the screen.

Some of the **features** of this program are:

*  Count the number of words in the file 
*  Count the number of sentences in the file (delimiters set as period and question mark)
*  The number of times each word occurs (frequency) in a document
*  The frequency of a specific word, which the user will input
*  Top 10 most common words in the file
*  TF-IDF (Term frequency - Inverse document frequency) - TF IDF evaluates the importance of each word in the document.
*  The average number of sentences in a file
*  The longest word in the input file
*  The length of the longest word in the input file
*  The shortest word in the input file
*  The frequency of each character in the input file

## Installation
```pip install nltk```

```pip install collections```

```pip install tfidf```

```pip install scikit-learn```

```pip install pandas```

Any additional library that is used in this program and needs to be installed on a local machine, can be installed using the format:

``` pip install <library name>```

## Usage

To run the program either directly click on the 'run' button on your IDE, or run the following command:

```python3 midterm.py```

- After running the program, do the following when prompted:

1. Enter the input file name
2. Enter the output file name
3. Enter the word whose frequency you want to know (number of times the specified word occurs in the document)

**Note:** In case of any unexpected errors/or having trouble running the program, please feel free to reach out to me at: s.umar@mail.utoronto.ca


## Sample Input and Output

The output on the screen:
[![1.png](https://i.postimg.cc/KYgWY2CK/1.png)](https://postimg.cc/wtg2WSqH)
[![2.png](https://i.postimg.cc/cHybgzNF/2.png)](https://postimg.cc/bGgT43rn)
[![3.png](https://i.postimg.cc/0QYHpCkP/3.png)](https://postimg.cc/vgmzyfxN)
[![4.png](https://i.postimg.cc/P5C36HX6/4.png)](https://postimg.cc/pmtJTgn8)
[![5.png](https://i.postimg.cc/fy52PTSP/5.png)](https://postimg.cc/xNJ3JQRG)
[![6.png](https://i.postimg.cc/SQGvRV1G/6.png)](https://postimg.cc/z3VjPwrL)

[![7.png](https://i.postimg.cc/8PPn6Wqg/7.png)](https://postimg.cc/XXm8MZjs)

Output.txt - The output file (does not contain the entire content of the file)

[![output-8.png](https://i.postimg.cc/6pFHgPTB/output-8.png)](https://postimg.cc/dhmmT48f)

Output of alphabet_frequency.csv

[![9-alpha-freq.png](https://i.postimg.cc/ZK7sFnSB/9-alpha-freq.png)](https://postimg.cc/xcmP90qn)

Output of TermFrequency.csv

[![10-tfidf.png](https://i.postimg.cc/VvzZ4bvM/10-tfidf.png)](https://postimg.cc/r0Y9wsSF)


## References

* https://www.tutorialspoint.com/how-to-find-the-longest-words-in-a-text-file-using-python#:~:text=Find%20the%20length%20of%20the,from%20the%20above%20words%20list.

* https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string

* 
