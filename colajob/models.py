
from colajob import mongo


class JobBullentin(mongo.Model):

    def __init__(self):
        super().__init__(__class__)
        self.schema = ['title','open_date','requirements']
