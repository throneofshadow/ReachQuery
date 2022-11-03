from python.data_loader import BlockQuery as Query

class ToQuery:
    """ Start simple, we want to input using a string the main path, the rat, the date, and the session.
        Outputs should be """
    def __init__(self):
        dir_path = 'C:\\Users\\bassp\\OneDrive\\Desktop\\Classification Project\\ReachProcess'
        rat = 'RM16'
        date = '09202019'
        session = 'S2'
        Query(dir_path, rat, date, session)


ToQuery()