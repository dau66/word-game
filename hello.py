import random

words = [
    # A
    'about', 'actor', 'adapt', 'adopt', 'adult', 'after', 'again', 'agent', 'agree', 'allow', 
    'alloy', 'along', 'amaze', 'among', 'anger', 'angle', 'angry', 'ankle', 'annoy', 'apple', 
    'apply', 'april', 'argue', 'arise', 'asset', 'avoid', 'awake', 'award', 'aware', 
    # B
    'based', 'basic', 'basin', 'beard', 'berry', 'birth', 'black', 'blade', 'blame', 'blood', 
    'board', 'bound', 'brain', 'brake', 'brass', 'brave', 'bread', 'break', 'bribe', 'brick', 
    'brief', 'broad', 'brown', 'brush', 'bunch', 'burst', 
    # C
    'camel', 'cargo', 'cause', 'cease', 'chain', 'chair', 'chalk', 'chart', 'cheap', 'check', 
    'chest', 'chief', 'child', 'china', 'claim', 'class', 'clean', 'clear', 'clock', 'cloth', 
    'cloud', 'color', 'cough', 'court', 'cover', 'crack', 'creep', 'crime', 'cross', 'cruel', 
    'crush', 'crust', 'curve',
    # D 
    'daily', 'dance', 'death', 'debit', 'delay', 'dense', 'depth', 'deter', 'dirty', 'ditch', 
    'doubt', 'drain', 'drama', 'dream', 'dress', 'drift', 'drill', 'drink',
    # E
    'eager', 'early', 'earth', 'eight', 'elder', 'empty', 'enemy', 'enter', 'entry', 'epoch',
    'equal', 'equip', 'error', 'event', 'every', 'exact', 'exist',
    # F
    'faith', 'false', 'fancy', 'farce', 'fault', 'favor', 'feast', 'feces', 'fever', 'fiber',
    'field', 'fifth', 'fifty', 'fight', 'fired', 'first', 'fixed', 'flame', 'flash', 'flask',
    'flesh', 'flint', 'flood', 'floor', 'flour', 'fluid', 'focus', 'force', 'forty', 'found',
    'frame', 'fresh', 'front', 'frost', 'fruit', 'funny', 
    # G
    'gland', 'glare', 'glass', 'gleam', 'glint', 'globe', 'glove', 'grain', 'grand', 'grass', 
    'grate', 'great', 'greed', 'green', 'greet', 'grief', 'gross', 'group', 'guard', 'guess', 
    'guest', 'guide',
    # H
    'habit', 'happy', 'harsh', 'heart', 'heavy', 'hedge', 'hinge', 'honey', 'horse', 'hotel',
    'house', 'human', 'humor', 'hurry', 'hyena',
    # I
    'ideal', 'image', 'index', 'inlet', 'inner', 'input', 'issue',
    # J
    'jelly', 'jewel', 'joint', 'judge', 'juice',
    # K
    'knife', 'knock',
    # L
    'labor', 'large', 'laugh', 'layer', 'lease', 'least', 'legal', 'level', 'lever', 'light',
    'limit', 'linen', 'liter', 'liver', 'local', 'locus', 'loose', 'lunar', 'lunch',
    # M
    'madam', 'magic', 'major', 'mania', 'march', 'match', 'maybe', 'means', 'metal', 'meter', 
    'might', 'miner', 'minor', 'mixed', 'model', 'moist', 'money', 'month', 'moral', 'mouth', 
    'music',
    # N
    'naked', 'nasty', 'nerve', 'never', 'night', 'noble', 'noise', 'north', 'noted', 'nurse',
    # O
    'occur', 'offer', 'olive', 'opera', 'opium', 'orbit', 'order', 'organ', 'other', 'outer',
    'owner',
    # P
    'paint', 'paper', 'party', 'paste', 'peace', 'pedal', 'pence', 'penny', 'peril', 'petal',
    'piano', 'place', 'plain', 'plane', 'plant', 'plate', 'point', 'pound', 'power', 'prank',
    'price', 'prick', 'prime', 'print', 'proof', 'prose', 'proud', 'prove', 'pupil',
    # Q
    'quack', 'quake', 'queen', 'quick', 'quiet', 'quite', 'quota', 'quote',
    # R
    'radio', 'range', 'rapid', 'ratio', 'razor', 'react', 'ready', 'refer', 'reign', 'repay',
    'reply', 'right', 'rival', 'river', 'rough', 'round', 'route', 'royal', 'ruler', 'rural',
    # S
    'salad', 'scale', 'scarp', 'scent', 'scold', 'screw', 'seize', 'sense', 'sepal', 'serum',
    'seven', 'shade', 'shake', 'shale', 'shame', 'share', 'sharp', 'shave', 'shear', 'sheep',
    'sheet', 'shelf', 'shell', 'shine', 'shirt', 'shock', 'shore', 'short', 'sight', 'silly',
    'since', 'skill', 'skirt', 'skull', 'slate', 'slave', 'sleep', 'slide', 'slope', 'small',
    'smash', 'smell', 'smile', 'smoke', 'snake', 'sniff', 'solar', 'solid', 'sorry', 'sound',
    'south', 'space', 'spade', 'spark', 'spoil', 'spoon', 'sport', 'stage', 'stain', 'stair',
    'stalk', 'stamp', 'stare', 'start', 'state', 'steam', 'steel', 'stern', 'stick', 'stiff',
    'still', 'stink', 'stone', 'store', 'storm', 'story', 'straw', 'study', 'sugar', 'sulky',
    'swear', 'sweet', 'swing',
    # T
    'table', 'taste', 'tense', 'their', 'there', 'these', 'thick', 'thief', 'thing', 'third',
    'those', 'three', 'thumb', 'tight', 'tired', 'toast', 'today', 'token', 'tongs', 'tooth',
    'total', 'touch', 'towel', 'tower', 'trace', 'track', 'trade', 'train', 'treat', 'trend',
    'trick', 'truck', 'trust', 'twice', 'twist',
    # U
    'under', 'unite', 'urban', 'urine', 'usage', 'usual', 'utter',
    # V
    'valid', 'value', 'valve', 'vapor', 'verse', 'vigor', 'vital', 'vodka', 'voice',
    # W
    'wagon', 'waste', 'watch', 'water', 'waver', 'wedge', 'wheel', 'where', 'which', 'while',
    'white', 'whose', 'widow', 'width', 'wince', 'woman', 'world', 'worry', 'worth', 'would',
    'wound', 'wrath', 'wreck', 'wrist', 'wrong',
    # Y
    'young', 'yours', 'youth', 'yyour',
    # Z
    'zebra'
]

def hint(str1, str2):
    i = 0
    j = 0
    c1 = 0
    c2 = 0
    list1 = list(str1)
    list2 = list(str2)
    while i < 5:
        while j < 5:
            if list1[i] == list2[j] and i == j:
                print('\033[32m' + list1[i] + '\033[0m', end='')
                c1 += 1
                break
            elif list1[i] == list2[j] and i != j:
                print('\033[32m' + list1[i] + '\033[0m',
                      end='')  # Print in green
                c2 += 1
                break
            j += 1
        if c1 == 0 and c2 == 0:
            print(list1[i], end='')
        c1 = 0
        c2 = 0
        j = 0
        i += 1
    return 0


correct = 'apple'
trial_count = 0
print('Guess the word')
print('Yellow is word choice is ok but, another location.\n Green is correct', end='')
while True:
    ans = input('\n')
    if (ans == 'giveup'):
        print('The answer is ' + correct + '\n')
        print('Trial counter is ' + str(trial_count) + '\n')
        break
    # elif (len(ans) != 5 or ans not in words):
    #     trial_count += 1
    #     print('try again', end='')
    #     continue
    elif (ans == correct):
        print('Correct!\n')
        print('Trial counter is ' + str(trial_count) + '\n')
        break
    else:
        hint(ans, correct)
        trial_count += 1
        continue
