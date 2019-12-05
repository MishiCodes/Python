def find_needle(haystack):
    # return 'found the needle at position {}' .format(haystack.index('needle'))
    return f'found the needle at position {haystack.index("needle")}'


print(find_needle(['hay', 'junk', 'hay', 'hay',
                   'moreJunk', 'needle', 'randomJunk']))
