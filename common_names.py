"""
Work with files has been completed in this file
"""


def names_read(file_name) :
    """
    This function returns lists of read data from two files
    >>> names_read(1)
    """
    if not isinstance(file_name, str) :
        return None
    file = open(file_name, encoding='utf8')
    file = [i for i in file]
    file = [elem_male.strip('\n') for elem_male in file]
    return file


def common_names(female_names, male_names) :
    """
    This function will sort the lists by
    conditions and write the result into a separate set
    >>> common_names(female_names=['App', 'Rem', 'Andry'], male_names=['App', 'Pep', 'Andry'])
    {'Andry', 'App'}
    """
    female_names = set(female_names)
    male_names = set(male_names)
    result = male_names & female_names
    letter = ['A', 'E', 'I', 'O', 'U', 'Y']
    result_final = [o for o in result if o[0] in letter]
    result_final = set(result_final)
    return result_final

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
