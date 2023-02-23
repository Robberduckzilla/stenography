import sys
from TTS.api import TTS
from pydub import AudioSegment
from random import shuffle
from itertools import chain


def get_segements_from_file(filename='text.txt', split_on='sentences', random=True):
    with open(filename, 'r') as f:
        segments=f.readlines()
    
    if split_on == 'lines':
        pass
    elif split_on == 'sentences':
        segments = list(chain([x.split('.') for x in segments]))
    elif split_on == 'words':
        segments = list(chain([x.split(' ') for x in segments]))
        # hack: merge short words like 'a' or 'it' with the following word
        # because the TTS model struggles with very short words on their own.
        segments_clone = []
        skip=False
        for i in range(len(segments)):
            if skip:
                skip = False
                continue
            if len(segments[i]) > 2:
                segments_clone.append(segments[i])
            else:
                segments_clone.append(' '.join(segments[i:i+2]))
                skip = True
        segments = segments_clone
    if random:
        shuffle(segments)
    return segments


def generate_wav(segments, silence_length=1000):
    working = AudioSegment.silent(1)
    silence = AudioSegment.silent(silence_length)

    models=TTS.list_models()
    model_name=models[7]
    tts=TTS(model_name)

    for segment in segments:
        tts.tts_to_file(segment, file_path='temp.wav')
        single_segment=AudioSegment.from_wav('temp.wav')
        working = working + single_segment + silence

    working.export('dictation.wav')


arguments = sys.argv[1:]

if arguments:
    try:
        filename=sys.argv[1]
    except:
        filename = 'text.txt'

    try: 
        split_on = sys.argv[2]
    except:
        split_on = 'sentences'
    
    try:
        random = True if sys.argv[3] == 'random' else False
    except:
        random = True
    try:        
        silence_length = int(sys.argv[4])
    except:
        silence_length = 1000


segments = get_segements_from_file(filename, split_on, random)
generate_wav(segments, silence_length)