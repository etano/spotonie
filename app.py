import logging
from tonie_api import TonieAPI


# set up detailed logging
logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)

api = TonieAPI('ethan.w.brown@gmail.com', 'TOOG3louw!vec5fler')
api.me  # show your information stored in toniecloud

# update all housholds, returns IDs of households
households = api.households_update()
household_id = [k for k, v in households.items() if v == "Ethans Haushalt"][0]

# update all creative tonies, returns IDs of creative tonies
tonies = api.households[household_id].creativetonies_update()
tonie_id = [k for k, v in tonies.items() if v == "Kreativ-Tonie"][0]

# list chapters on creative tonie
print(api.households[household_id].creativetonies[tonie_id].chapters)

# upload a new audio file
# api.households['yourHouseholdID'].creativetonies['yourTonieID'].upload('file.mp3', 'Test 123')

# sort chapters by title
# api.households['yourHouseholdID'].creativetonies['yourTonieID'].sort_chapters('title')
