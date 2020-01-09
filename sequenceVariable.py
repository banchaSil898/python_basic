def sequence_tuple():
    # Tuples
    tuples_family = ('Somsak', 'Supatra', 'Bancha', 'Thanyawat', 'Nutcha')
    print('(( Tuples Sequence BEGIN ))')
    print(tuples_family[0])
    print(tuples_family[1])
    print(tuples_family[2])
    print(tuples_family[3])
    print(tuples_family[4])
    print('(( Tuples Sequence END ))')
    # Tuples


def sequence_list():
    # Lists
    print('[[ Lists Sequence BEGIN ]]')
    lists_family = ['Somsak', 'Supatra', 'Bancha', 'Thanyawat', 'Nutcha']
    lists_family.pop()  # remove'Nutcha'
    lists_family.pop(1)  # remove 'Supatra'

    lists_family.append('Nutcha')  # insert 'Nutcha' as last
    lists_family.insert(1, 'Supatra')  # insert 'Supatra' as [1]

    print(lists_family[0])
    print(lists_family[1])
    print(lists_family[2])
    print(lists_family[3])
    print(lists_family[4])
    list_sort = lists_family
    list_sort.sort()
    print('sort')
    print(list_sort)
    print('revert')
    list_reverse = lists_family
    list_reverse.reverse()
    print(list_reverse)
    print('[[ Lists Sequence END ]]')
    # Lists


def sequence_dictionary():
    # Dictionary
    dict_family = {
        "father": 'Somsak',
        "mother": 'Supatra',
        "son1st": 'Bancha',
        "son2nd": 'Thanyawat',
        "gndDaughter": 'Nutcha'
    }
    print(":: Dictionary BEGIN ::")
    print(dict_family["father"])
    print(dict_family["mother"])
    print(dict_family["son1st"])
    print(dict_family["son2nd"])
    print(dict_family["gndDaughter"])
    print(":: Dictionary END ::")
    # Dictionary
