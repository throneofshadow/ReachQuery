from python.data_loader import BlockQuery as Query

class ToQuery:
    """ Start simple, we want to input using a string the main path, the rat, the date, and the session.
        Outputs should be """
    def __init__(self):
        self.rat_name, self.rat_date, self.rat_session = None, None, None
        self.get_manual_information()
        self.dir_path = 'C:\\Users\\bassp\\OneDrive\\Desktop\\Classification Project\\ReachProcess'
        self.rat_name = 'RM16'
        self.rat_date = '09202019'
        self.rat_session = 'S2'
        query_types = [False, False, False]
        try:
            Query(self.dir_path, self.rat_name, self.rat_date, self.rat_session, query_types)
        except:
            print('Unable to process data for your variable combinations. Please use valid entries. ')

    def get_manual_information(self):
        print('Welcome to ReachQuery V1.0. To change the data directory from your current working directory, please enter 0.')
        iid = input()
        if iid == 0:
            print('Please enter working directory. ')
            self.dir_path = str(input())
        print(' To get started, enter the rat you would like to query over. For example, RM16 ')
        self.rat_name = str(input())
        print('Thanks, what is the rat date? For example, 09192019 is the date September 19, 2019. ')
        self.rat_date = str(input())
        print('And what is the rat session? For example, S2. ')
        self.rat_session = str(input())
        print('Thanks, we are looking that information up. ')


ToQuery()