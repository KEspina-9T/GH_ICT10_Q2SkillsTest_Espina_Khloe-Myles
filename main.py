from pyscript import display #type:ignore

def organizations(e):
    orgs = {
        "1": {
            'Name of the club':'Atelier Fashion Guild',
            'Description':'The Atelier Fashion Guild is an Organization where students can express their creativity, and identity through fashion.',
            'Meeting time':'1 p.m - 3 p.m',
            'Location': 'Magnus Building, 4th floor, Fashion Workshop',
            'Club Moderator':'Prof. Marielle Greenwood.',
            'Number of members':'30'
        },
        "2": {
            'Name of the club':'Ivory Debate Union',
            'Description':'The Ivory Debate Union is an Organization where students can put to use all they have learned in the English class from previous years. Here they can test their critical thinking skills through debates, researches, etc.',
            'Meeting time':'2 p.m - 3 p.m',
            'Location': 'Lux Building, 8th Floor, room 802',
            'Club Moderator':'Prof. Crew Kensington.',
            'Number of members':'40'
        },
        "3": {
            'Name of the club':'Ministry of Sciences',
            'Description':'The Ministry of Sciences is an Organization where students can make use of their critical thinking skills in order to conduct science experiments and create research papers and studies for future reference in the Science World.',
            'Meeting time':'2 p.m - 4 p.m',
            'Location': 'Factum Building, 7th floor, Science Laboratory',
            'Club Moderator':'Prof. Hannah Wells',
            'Number of members':'30'
        }
    }


selected =  document.getElementById('org').value #type:ignore

display(orgs[selected], target="output") # type: ignore

