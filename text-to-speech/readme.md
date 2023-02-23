## Text-to-speech for stenography practise

1. Install dependencies (TTS and pydub)

    `pip3 install TTS pydub`

    latest TTS (0.9.0) Requires Python >=3.7.0, <3.11.
2. Find a text file you want the program to dictate, and put it in the same folder as the script (default: text.txt)

3. call the script from the command line with space-separated arguments

    `python3 dictate.py text.txt sentences random 1000`

    Arguments are:
        
        - Filename (default text.txt) - name of the file you want to read in
        
        - Segmentation (default sentences) - where to insert pauses, valid options are sentences, words, and lines
        
        - random yes/no (default random) - if 'random', the program will shuffle the words/lines in a random order. If anything other than 'random', it won't
        
        - silence length in milliseconds (default 1000) - how long the pauses will be between words/lines/sentences. If using 'words' segmentation, the average word length is 1100ms, so you can use a target words-per-minute to generate the correct silence length using: (60000/WPM) - 1100