import string
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter 


def writeTranscriptToTxt():
    videoID = input("Enter the video ID (the value after 'v=' in the YouTube video URL) ")
    transcript = YouTubeTranscriptApi.get_transcript(videoID)
    formatter = TextFormatter()
    text_formatted = formatter.format_transcript(transcript)

    with open('output.txt', 'w', encoding='utf-8') as text_file:
        text_file.write(text_formatted)
    


def noPuncuations(line):
    for character in string.punctuation:
        line = line.replace(character, "")
    return line

def readFile():
    wordCountDict = {}
    with open('output.txt', 'r', encoding='utf-8') as text_file:
        for line in text_file:
            line = noPuncuations(line)
            words = line.split()
            for splitWord in words:
                splitWord = splitWord.lower()
                if splitWord not in wordCountDict:
                    wordCountDict[splitWord] = 0
                wordCountDict[splitWord] += 1
    wordCountGivenWord(wordCountDict)


def wordCountGivenWord(wordCountDict):
    
    word = input("Enter a word you want to know the frequency of ").lower()
    print(wordCountDict[word])





writeTranscriptToTxt()
readFile()