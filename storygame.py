#The link to the module https://pypi.org/project/pag/
from pag import GameWorld
from pag import CommandLineInterfacee
from pag import classes

#Location list 
gameworld = GameWorld(locations=classes.location_list)
cli = CommandLineInterface(gameworld)
#We are creating the ToiletPaper 
class ToiletPaper(classes.Item):
    def __init__(self):
        super().__init__(name='toilet paper',
                         description='The toilet paper is labeled "X-t'
                         'raSoft.',
                         loc_description='A roll of toilet paper is in '
                         'the room.',
                         weight=1)

#Locations
home = classes.Location('Home', start=True, show_name_when_exit=True)
home.description = 'You\'re at home.'
bathroom = classes.Location('Bathroom', items=[ToiletPaper()], show_name_when_exit=True)
bathroom.description = 'You\'re in the bathroom.'
home.exits = {'south': bathroom}
bathroom.exits = {'north': home}

cli.play()
