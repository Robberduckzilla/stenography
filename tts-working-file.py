from TTS.api import TTS
from pydub import AudioSegment
from random import shuffle

# import from text file
# Shuffle word order
# Longer line breaks for new lines

WPM = 30
random = True
fuck_around = False
average_word_length = 1100
silence_length = (60000 / WPM) - average_word_length

working = AudioSegment.silent(1)
models=TTS.list_models()
model_name=models[7]
tts=TTS(model_name)

silence = AudioSegment.silent(silence_length)

# open file and read words
with open('typing.txt', 'r') as f:
    words=f.readline()
words=words.split(' ')
words = [x for x in words if x]
if random:
    shuffle(words)


for word in words:
    word = word.title()
    if isinstance(word, list):
        word = word[0]
    if '.' not in word:
        word = word + '.'
    
    tts.tts_to_file(word, file_path='one_word.wav')
    if not fuck_around:
        test_audio = AudioSegment.from_file('one_word.wav')
        while test_audio.duration_seconds > 2:
            tts.tts_to_file(word, file_path='one_word.wav')
            test_audio = AudioSegment.from_file('one_word.wav')
            
    one_word=AudioSegment.from_wav('one_word.wav')
    working = working + one_word + silence

working.export('dictation.wav')