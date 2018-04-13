#Database of animals sorted by class and in alphabetical order
animals = {
'bird' : { ### CLASS BIRD ###

'crow': {
'colors':["black"],
'size':["small"],
'keyword':[]},

'eagle': {
'colors':[],
'size':["medium"],
'keyword':["sigil of america"]},

'falcon': {
'colors':[],
'size':["big"],
'keyword':[]}

},
'fish' : { ### CLASS FISH ###
'salmon': {
'colors':[],
'size':["small"],
'habitat':["waterfall","river"]}
},
'insect' : { ### CLASS INSECT ###
'ant': {'colors':[], 'size':["small"],'movement':["walking"], 'limbs':["6 limbs"], 'wings':["no wings"], 'keyword':[]},

'bee': {'colors':[], 'size':["small"], 'movement':["flying"], 'limbs':["6 limbs"], 'wings':["wings"], 'keyword':["honey"]},

'bumblebee': {'colors':[], 'size':[], 'movement':["flying"], 'limbs':["6 limbs"], 'wings':["wings"], 'keyword':[]},

'butterfly': {'colors':[], 'movement':["flying"], 'size':["small"], 'limbs':["6 limbs"], 'wings':["wings"], 'keyword':[]},

'cicadas': {'colors':[], 'size':[], 'movement':["walking"], 'limbs':["6 limbs"], 'wings':["wings"], 'keyword':[]},

'cricket': {'colors':[], 'size':[], 'movement':["jumping"], 'limbs':["6 limbs"], 'wings':["wings"], 'keyword':[]},

'dragonfly': {'colors':[], 'size':[], 'movement':["flying"], 'limbs':["6 limbs"], 'wings':["wings"], 'keyword':[]},

'flea': {'colors':[], 'size':[], 'movement':["jumping"], 'limbs':["6 limbs"], 'wings':["no wings"], 'keyword':[]},

'fly': {'colors':[], 'size':["small"], 'movement':["flying"], 'limbs':["6 limbs"], 'wings':["wings"], 'keyword':[]},

'grasshooper': {'colors':[], 'size':["small"], 'movement':["jumping"], 'limbs':["6 limbs"], 'wings':["wings"], 'keyword':[]},

'ladybird': {'colors':[], 'size':[], 'movement':["flying"], 'limbs':["6 limbs"], 'wings':["wings"], 'keyword':[]},

'mantis': {'colors':[], 'size':[], 'movement':["walking"], 'limbs':["6 limbs"], 'wings':["no wings"], 'keyword':[]},

'mosquito': {'colors':[], 'size':["small"], 'movement':["flying"], 'limbs':["6 limbs"], 'wings':["wings"], 'keyword':[]},

'spider': {'colors':[], 'size':["small"], 'movement':["walking"], 'limbs':["8 limbs"], 'wings':["no wings"], 'keyword':[]},

'termite': {'colors':[], 'size':[], 'movement':["walking"], 'limbs':["6 limbs"], 'wings':["no wings"], 'keyword':[]},

'worm': {'colors':[], 'size':[], 'movement':["crawling"], 'limbs':["no limbs"], 'wings':["no wings"], 'keyword':[]}
},

'mammal' : { ### CLASS MAMMAL ###

'bat': {'colors':["black"], 'location':["caves"], 'size':["small"], 'behaviour':["group"], 'dietary':["omnivorous"], 'epiderm':[], 'keyword':[]},

'bear': {'colors':["brown"], 'location':["forest", "moutain"], 'size':["large"], 'behaviour':["alone"], 'dietary':["carnivorous"], 'epiderm':["fur"], 'keyword':[]},

'cat': {'colors':["many colors"], 'location':["cities"], 'size':["small"], 'behaviour':["alone"], 'dietary':["omnivorous"], 'epiderm':["fur"], 'keyword':[]},

'cow': {'colors':["many colors"], 'location':["grassland"], 'size':["large"], 'behaviour':["group"], 'dietary':["herbivorous"], 'epiderm':["skin"], 'keyword':[]},

'deer': {'colors':["brown"], 'location':["forest"], 'size':["medium"], 'behaviour':["group"], 'dietary':["herbivorous"], 'epiderm':["fur"], 'keyword':[]},

'dog': {'colors':["many colors"], 'location':["cities"], 'size':["small"], 'behaviour':["group"], 'dietary':["omnivorous"], 'epiderm':["fur"], 'keyword':[]},

'dolphin': {'colors':["blue", "grey"], 'location':["sea", "water"], 'size':["medium"], 'behaviour':["group"], 'dietary':["omnivorous"], 'epiderm':["skin"], 'keyword':[]},

'elephant': {'colors':["grey"], 'location':["savannah"], 'size':["large"], 'behaviour':["group"], 'dietary':["herbivorous"], 'epiderm':["skin"], 'keyword':["ivory"]},

'fox': {'colors':["orange", "red"], 'location':["forest"], 'size':["small"], 'behaviour':["alone"], 'dietary':["omnivorous"], 'epiderm':["fur"], 'keyword':[]},

'koala': {'colors':["brown", "grey"], 'location':["forest"], 'size':["small"], 'behaviour':[], 'dietary':["herbivorous"], 'epiderm':["fur"], 'keyword':[]},

'hippopotamus': {'colors':["grey"], 'location':["savannah", "water"], 'size':["large"], 'behaviour':["group"], 'dietary':["omnivorous"], 'epiderm':["skin"], 'keyword':[]},

'horse': {'colors':["many colors"], 'location':["grassland"], 'size':["medium"], 'behaviour':["group"], 'dietary':["herbivorous"], 'epiderm':["fur"], 'keyword':[]},

'kangaroo': {'colors':["brown"], 'location':["grassland","desert"], 'size':["medium"], 'behaviour':["group"], 'dietary':["herbivorous"], 'epiderm':["fur"], 'keyword':[]},

'lion': {'colors':["yellow", "brown"], 'location':["savannah"], 'size':["medium"], 'behaviour':["group"], 'dietary':["carnivorous"], 'epiderm':["fur"], 'keyword':[]},

'otter': {'colors':["brown"], 'location':["river", "water"], 'size':["small"], 'behaviour':["group"], 'dietary':["omnivorous"], 'epiderm':["fur"], 'keyword':[]},

'panda': {'colors':["black and white"], 'location':["forest"], 'size':["medium"], 'behaviour':["alone","group"], 'dietary':["herbivorous"], 'epiderm':["fur"], 'keyword':[]},

'rabbit': {'colors':["many colors"], 'location':["forest", "grassland"], 'size':["small"], 'behaviour':["alone"], 'dietary':["herbivorous"], 'epiderm':["fur"], 'keyword':[]},

'raccoon': {'colors':["white","black","white"], 'location':["forest"], 'size':["small"], 'behaviour':["alone"], 'dietary':["omnivorous"], 'epiderm':["fur"], 'keyword':[]},

'rhinoceros': {'colors':["grey"], 'location':["savannah"], 'size':["big"], 'behaviour':["alone","group"], 'dietary':["herbivorous"], 'epiderm':["skin"], 'keyword':["ivory"]},

'tiger': {'colors':["yellow", "orange","black","white"], 'location':["forest","jungle"], 'size':["medium"],
'behaviour':["alone"], 'dietary':["carnivorous"], 'epiderm':["fur"], 'keyword':[]},

'whale': {'colors':["blue", "grey"], 'location':["sea", "water"], 'size':["very large"], 'behaviour':["group"], 'dietary':["omnivorous"], 'epiderm':["skin"], 'keyword':[]},

'zebra': {'colors':["black and white"], 'location':["savannah"], 'size':["medium"], 'behaviour':["group"], 'dietary':["herbivorous"], 'epiderm':["fur"], 'keyword':[]}
}
}
