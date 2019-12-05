names = ['Jasmine', 'Alexandra', 'Bojana']
locations = ['stockholm', 'goteborg', 'helsingborg']

def lists_to_dict(names, locations):

    my_dict = {names[n]: locations[n] for n in range(len(names))}
    return my_dict

def json_format(names, locations):
    new_dict = {names[n]: {'location': locations[n]}
                for n in range(len(names))}
    return new_dict

print(lists_to_dict(names, locations))
print(json_format(names, locations))


# -------------------------- METHOD 2: -----------------------

# def lists_to_dict(names, locations):

#     my_dict = {name: location for name, location in zip(names, locations)}
#     return my_dict

# def json_format(names, locations):

#     new_dict = {name: {'location': location}
#                 for name, location in zip(names, locations)}
#     return new_dict

# print(lists_to_dict(names, locations))
# print(json_format(names, locations))
