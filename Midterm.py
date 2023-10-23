# Import and install relevant libraries
import re
import string
import collections
from collections import Counter
import pandas as pd
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer


#-----------------------------------------------------------------------------------------------------
# Input: Name of the input file, entered by user
# Output: content of the file
# Description:
#           This function is responsible for reading the contents of the specified file
#------------------------------------------------------------------------------------------------------

def read_file(filename):
    with open(filename, 'r') as file:
        # read the file and stores the content in variable chars as a string
        chars = file.read()
    return chars

#------------------------------------------------------------------------------------------------------
# Input: Name of the output file, entered by user
# Output: The results of the entire program will be displayed in this file
# Description:
#           This function is responsible for writing the results of this program to a new file,
#           The name of the file will be specified by the user.
#-------------------------------------------------------------------------------------------------------

def write_file(output_Filename, output_data):
    with open(output_Filename, 'w') as file:
        file.write(output_data)

#-------------------------------------------------------------------------------------------------------
# Input: Content of the input file
# Output: The total count of the words in the file
# Description:
#         This function is responsible for counting the number of total words in the user specified file
#--------------------------------------------------------------------------------------------------------

def wordCount(chars):
    # Split the file content. The delimiter is white space
    words = chars.split()
    wordCount = 0
    for word in words:
        wordCount += 1
        
    return wordCount

#--------------------------------------------------------------------------------------------------------
# Input: Content of the input file
# Output: The total number of sentences in the input file
# Description:
#           This function is responsible for counting the total number of sentences in the file.
#           We have the delimiter as "?" and "." so whenever the program comes across a period
#           or a question mark, it will count it as a new sentence.
#---------------------------------------------------------------------------------------------------------

def num_sentences(chars):
    # Split the text using the regex by using period or question mark as delimiters
    num_of_sent = re.split(r'[.?]+', chars)
    
    # Filter empty sentences
    num_of_sent = [sentence for sentence in num_of_sent if sentence.strip()]
    
    return len(num_of_sent)

#--------------------------------------------------------------------------------------------------------
# Input: Content of the input file
# Output: The total number of times each word appears in the input file
# Description:
#           This function is responsible for counting the total number of times each word appears in 
#           the input text file. It is basically counting the frequency of each word in the file.
#---------------------------------------------------------------------------------------------------------

def frequency(chars):
    words = chars.lower().split()
    # Get the stopwords
    stoplist = set(stopwords.words('english'))
    
    # Create a translation table to remove the punctuation from words
    translate_table = str.maketrans('','',string.punctuation)
    
    # Remove the stopwords and punctuation
    remove_stopwords = [word.translate(translate_table) for word in words if word not in stoplist]
    
    # Count the frequency of each word
    word_freq = Counter(remove_stopwords)
    
    return word_freq

#--------------------------------------------------------------------------------------------------------
# Input: Content of the input file
# Output: The frequency of the word specified by the user
# Description:
#           This function is responsible for counting the total number of times a specific word appears
#           in the file. The specific word will be asked to the user.
#---------------------------------------------------------------------------------------------------------

def user_word_frequency(chars):
    words = chars.lower().split()
    
    # Get the stopwords
    stoplist = set(stopwords.words('english'))
    
    # Create a translation table to remove the punctuation from words
    translate_table = str.maketrans('','',string.punctuation)
    
    # Remove the stopwords and punctuation
    remove_stopwords = [word.translate(translate_table) for word in words if word not in stoplist]
    
    # Count the frequency of each word
    word_freq = Counter(remove_stopwords)
    
    # Take user input
    userinput = input("Please enter the word you want to calculate the frequency for: ")
    
    # Get frequency of the word user specified
    freq_of_word = word_freq[userinput]
    
    return "The word {} appears {} times.".format(userinput, freq_of_word)

#----------------------------------------------------------------------------------------------------------
# Input: Content of the input file
# Output: A dataframe consisting of the top 10 words which occured the most number of times in a file
# Description:
#           This function is responsible for counting the total number of times a word appears in the file.
#           It then sorts them in descending order and outputs the top 10 most occuring words.
#-----------------------------------------------------------------------------------------------------------

def frequent_words(chars):
    # Call the frequency function to get the frequencies of all the words
    word_count = frequency(chars)
    
    #Sort words by frequency in descending order
    sort_count = sorted(word_count.items(), key = lambda x: x[1], reverse = True)
    common_words = sort_count[:10]
    
    # display the 10 most common words as a data frame
    df = pd.DataFrame(common_words, columns=['Word', 'Frequency'])
    return df
    
#--------------------------------------------------------------------------------------------------------
# Input: Content of the input file
# Output: TermFrequcny.csv: This new file will be created and it will containg the 
# Term Frequncy - Inverse Document Frequency (TF-IDF) of each word in the document.
# Description:
#           This function is responsible for calculating the Tf-idf value for each word in the document
#           and then displaying it as a dataframe.
#---------------------------------------------------------------------------------------------------------

def termFrequency_idf(chars):
    words = chars.lower().split()
    
    # Get the stopwords
    stoplist = set(stopwords.words('english'))
    
    # Create a translation table to remove the punctuation from words
    translate_table = str.maketrans('','',string.punctuation)
    
    # Remove the stopwords and punctuation
    remove_stopwords = [word.translate(translate_table) for word in words if word not in stoplist]
    processed_text = " ".join(remove_stopwords)
    
    # Create a TF-IDF vectorizer
    vectorizer = TfidfVectorizer()
    
    # Fit and transform the processed text
    tfidf_matrix = vectorizer.fit_transform([processed_text])
    
    # Get the TF-IDF values for all words in the document
    feature_names = vectorizer.get_feature_names_out()
    tfidf_values = tfidf_matrix.toarray()[0]
    
    # Create a DataFrame to display the words and their TF-IDF scores
    tfidf_df = pd.DataFrame({'Word': feature_names, 'TF-IDF': tfidf_values})
    tfidf_df.to_csv('TermFrequency.csv', header=True, index=False)
    
    return tfidf_df
    
#--------------------------------------------------------------------------------------------------------
# Input: Content of the input file
# Output: The average number of words in a sentence for the entire file
# Description:
#           This function is responsible for calculating the average number of words in a sentence for
#           a given input file. If the file is empty, it returns a 0
#---------------------------------------------------------------------------------------------------------

def avg_words_in_sent(chars):
    # Split the text into sentences
    sentences = nltk.sent_tokenize(chars)
    
    # Loop through each sentence and count the words
    count_word = [len(nltk.word_tokenize(sentence)) for sentence in sentences]
    
    if count_word:
        # calculate the average word count
        avg_word_count = sum(count_word) / len(count_word)
        return avg_word_count
    else:
        # return 0 if empty file/no sentences
        return 0
    
#--------------------------------------------------------------------------------------------------------
# Input: Content of the input file
# Output: The longest word in the input file
# Description:
#           This function is responsible for returning the longest word in the text file.
#---------------------------------------------------------------------------------------------------------

def longest_word(chars):
    words = chars.split()
    if not words:
        return None  
    longest = words[0]
    
    # Remove punctuation from the word using the translation table
    translate_table = str.maketrans('','',string.punctuation)
    for word in words:
        word = word.translate(translate_table)
        
        if len(word) > len(longest):
            longest = word 
    return longest

#--------------------------------------------------------------------------------------------------------
# Input: Content of the input file
# Output: The length of the longest word in the input file
# Description:
#           This function is responsible for returning the length of the longest word in the test file.
#---------------------------------------------------------------------------------------------------------

def length_longest_word(chars):
    words = chars.split()
    if not words:
        return None  
    longest = words[0]
    
     # Remove punctuation using a translation table
    translate_table = str.maketrans('','',string.punctuation)
    for word in words:
        word = word.translate(translate_table)
        
        if len(word) > len(longest):
            longest = word 
    return len(longest)

#--------------------------------------------------------------------------------------------------------
# Input: Content of the input file
# Output: The shortest word in the input file
# Description:
#           This function is responsible for returning the shortest word in the text file.
#---------------------------------------------------------------------------------------------------------

def shortest_word(chars):
    words = chars.split()
    
    if not words:
        return None
    
    shortest_word = words[0]
    for word in words:
        if len(word) < len(shortest_word):
            shortest_word = word
            
    return shortest_word

#--------------------------------------------------------------------------------------------------------
# Input: Content of the input file
# Output: alphabet_frequcny.csv: This new file will be created and it will contain the frequency of each
# "character" in the file.
# Description:
#           This function is responsible for calculating the frequency of each character in the file.
#           It will return the data frame in the output file, on the screen to the user, and will create
#           a new file called "alphabet_frequency.csv" which will contain the output.
#---------------------------------------------------------------------------------------------------------

def count_chars(chars):
    
    # Convert to lowercase
    chars = chars.lower()
    
    # Remove all non-alphabetical characters
    chars = ''.join(filter(str.isalpha, chars))

    # 3. Calculate the alphabet frequencies
    alphabet_freq = collections.Counter(chars)

    # 4. Create a table to save as a csv file
    table = pd.DataFrame([{'Character': char, 'Frequency': freq} for char, freq in alphabet_freq.items()])
    table.to_csv('alphabet_frequency.csv', header=True, index=False)
    
    return table

# Main
    
if __name__ == "__main__":    
    
    filename = input("Please enter the name of the input file:  ")
    output_Filename = input("Please enter the name of the output file: ")
    
    
    chars = read_file(filename)
    
    disp_WordCount = "Total word count: {}\n".format(wordCount(chars))
    disp_TotalSentences = f"Total number of sentences:{num_sentences(chars)}\n"
    disp_longestWord = f"Longest word:{longest_word(chars)}\n"
    disp_longest_length_word = f"Length of the longest word:{length_longest_word(chars)}\n"
    disp_shortestWord = f"Shortest word:{shortest_word(chars)}\n"
    disp_count_chars = f"{count_chars(chars)}\n"
    disp_freqWords = f" Top 10 most common words are: \n"
    disp_freqWords += f"{frequent_words(chars)}\n"
    disp_tfIDF = f"The term frequency of the words in the document are: \n"
    disp_tfIDF += f"{termFrequency_idf(chars)}\n"
    disp_avgWordsInSen = f"The average words in a senternce: {avg_words_in_sent(chars)}\n"
    
    result = frequency(chars)
    disp_frequency = ""
    for word,count in result.items():
        disp_frequency += f" '{word}' : {count}\n"
        
    disp_userWord_freq = f"{user_word_frequency(chars)}\n"
    
    print(disp_WordCount)
    print(disp_TotalSentences)
    print(disp_longestWord)
    print(disp_longest_length_word)
    print(disp_shortestWord)
    print(disp_count_chars)
    print(disp_tfIDF)
    print(disp_avgWordsInSen)
    print(disp_frequency)
    print(disp_userWord_freq)
    print(disp_freqWords)
    
    
    # Call write_file function to write the results to the file
    output_data1 = disp_WordCount + disp_TotalSentences + disp_longestWord + disp_longest_length_word + disp_shortestWord + disp_count_chars + disp_frequency + disp_userWord_freq + disp_freqWords + disp_tfIDF + disp_avgWordsInSen
    
    write_file(output_Filename, output_data1)

