# U.S states and abbreavitions
# Common module as I can't find one that is just these

class state:
    def __init__(self,name:str,abbr:str) -> None:
        self.name = name
        self.abbr = abbr
    def get_name(self):
        return self.name
    def get_abbr(self):
        return self.abbr

states = [
    state('Alabama','AL'),
    state('Alaska','AK'),
    state('American Samoa','AS'),
    state('Arizona','AZ'),
    state('Arkansas','AR'),
    state('Colorado','CO'),
    state('Connecticut','CT'),
    state('Delaware','DE'),
    state('District of Columbia','DC'),
    state('Federated States of Micronesia','FM'),
    state('Florida','FL'),
    state('Georgia','GA'),
    state('Guam','GU'),
    state('Hawaii','HI'),
    state('Idaho','ID'),
    state('Illinois','IL'),
    state('Indiana','IN'),
    state('Iowa','IA'),
    state('Kansas','KS'),
    state('Kentucky','KY'),
    state('Louisiana','LA'),
    state('Maine','ME'),
    state('Marshall Islands','MH'),
    state('Maryland','MD'),
    state('Massachusetts','MA'),
    state('Michigan','MI'),
    state('Minnesota','MN'),
    state('Mississippi','MS'),
    state('Missouri','MO'),
    state('Montana','MT'),
    state('Nebraska','NE'),
    state('Nevada','NV'),
    state('New Hampshire','NH'),
    state('New Jersey','NJ'),
    state('New Mexico','NM'),
    state('New York','NY'),
    state('North Carolina','NC'),
    state('North Dakota','ND'),
    state('Northern Mariana Is.','MP'),
    state('Ohio','OH'),
    state('Oklahoma','OK'),
    state('Oregon','OR'),
    state('Palau','PW'),
    state('Pennsylvania','PA'),
    state('Puerto Rico','PR'),
    state('Rhode Island','RI'),
    state('South Carolina','SC'),
    state('South Dakota','SD'),
    state('Tennessee','TN'),
    state('Texas','TX'),
    state('Utah','UT'),
    state('Vermont','VT'),
    state('Virginia','VA'),
    state('Virgin Islands','VI'),
    state('Washington','WA'),
    state('West Virginia','WV'),
    state('Wisconsin','WI'),
    state('Wyoming','WY')
]

abbrs = []
names = []

def get_abbr_list(return_list:bool=False):
    if len(abbrs) == 0:
        for s in states:
            abbrs.append(s.get_abbr())
    if return_list == True:
        return abbrs

def get_name_list(return_list:bool=False):
    if len(names) == 0:
        for s in states:
            names.append(s.get_name())
    if return_list == True:
        return names