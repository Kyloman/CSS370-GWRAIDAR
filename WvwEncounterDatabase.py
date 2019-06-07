#Class description:
#Store all the WvW encounter data with Details information in the database, provide the ability to view and add the WvW Encounter.

#Required interface:
#WvwEncounter parseLog(LogFile file)

#Parameters:
# 1. WvW encounter: WvW Encounter is required to know what to add.
# 2. LogFile file: file that user inputs

class WvwEncounterDatabase(EncounterDatabase):

    wvwEncounter = WvwEncounter() #WvwEncounterDatabase has a relationship with WvwEncounter
    
    def getWvWEncounterList():
        return WvWEncounterListPage
    
    def add(WvwEncounter we):
        pass

