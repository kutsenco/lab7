"""
arr
"""

def dict_reader_tuple(file_dict):
    """
    doc
    """
    file = open(file_dict, encoding='utf8')
    file = [i for i in file]
    file = [j.strip('\n') for j in file]
    result = []
    for i in range(len(file)) :
        file[i] = file[i].split(' ')
        file[i][1] = int(file[i][1])
        a = file[i][2:]
        file[i] = file[i][:2]
        file[i].append(a)
        pep = (file[i][0], file[i][1], file[i][2])
        result.append(pep)
    return result

def dict_reader_dict(file_dict):
    """
    doc
    """
    result = {}
    for i in file_dict:
        if file_dict[0]:
            result[len(file_dict[0])] = set()
        result[file_dict[0]].update(file_dict[1])
    result = {i:result[i] for i in sorted(result)}
    return result

def dict_invert(dct):
    """
    >>> dict_invert({'WATER':{('W','A','T','E','R')}})
    {1: {('WATER', ('W','A','T','E','R'))}}
    >>> dict_invert({'AABERG': {('AA1', 'B', 'ER0', 'G')}, 'A.': {('EY1',)},
    'A': {('EY1',), ('AH0',)}, 'A42128': {('EY1', 'F', 'AO1',
    'R', 'T', 'UW1', 'W', 'AH1', 'N', 'T', 'UW1', 'EY1', 'T')},
    'AAA': {('T', 'R', 'IH2', 'P', 'AH0', 'L', 'EY1')}})
    {1: {('A.', ('EY1',)), ('AABERG', ('AA1', 'B', 'ER0', 'G')), ('AAA', ('T', 'R', 'IH2', 'P', 'AH0', 'L', 'EY1')),
    ('A42128', ('EY1', 'F', 'AO1', 'R', 'T', 'UW1', 'W', 'AH1', 'N', 'T', 'UW1', 'EY1', 'T'))}, 
    2: {('A', ('EY1',)), ('A', ('AH0',))}}
    >>> dict_invert(dict_reader_tuple('cmudict.txt')) == dict_invert(dict_reader_dict('cmudict.txt'))
    True   
    """
    if isinstance(dct, dict):
        result = {}
    elif isinstance(dct, list):
        result_app = {}
        for i in dct:
            if i[0] not in dct:
                result_app[i[0]] = set()
            result_app[i[0]].update({tuple(i[2])})
        dct = result_app
        result = {}
    for i in dct:
        if len(dct[i]) not in dct:
            result[len(dct[i])] = set()
        result[len(dct[i])].update(zip([i]*len(dct[i], dct[i])))
    result = {i:result[i] for i in sorted(result)}
    return result

if __name__=="__main__" :
    import doctest
    print(doctest.testmod())
