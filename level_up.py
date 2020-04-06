attribute_ls = [
    (8,-1),
    (10,0),
    (12,1),
    (14,2),
    (16,3),
    (18,4),
    (20,5)
]

class_ls = [
    'Barbarian', 
    'Bard', 
    'Cleric',
    'Druid',
    'Fighter',
    'Monk',
    'Paladin',
    'Ranger',
    'Rouge',
    'Sorcerer',
    'Warlock',
    'Wizard'
]

character_dc = {
    'Thell' : {
        'Level' : 2,
        'Class' : 'Cleric',
        'Attributes' : {
            'str' : 14,
            'dex' : 8,
            'con' : 15,
            'int' : 8,
            'wis' : 17,
            'chr' : 13
        }
    }
}

def get_modifier(character, attribute):
    att_val = character_dc[character]['Attributes'][attribute] #getting the value of the specified attribute
    modifier = max(filter(lambda i: i[0] <= att_val, attribute_ls)) #filtering values and returning the greatest one
    return modifier[1]  #selecting the second element from the tuple returned from the line above

def get_attribute(character, attribute):
    att_val = character_dc[character]['Attributes'][attribute] 
    return att_val

print(get_attribute('Thell', 'str'))
print(get_modifier('Thell', 'str'))