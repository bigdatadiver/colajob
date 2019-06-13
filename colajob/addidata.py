
<<<<<<< HEAD
from colajob import models


class JobBullentin(models.JobBullentin):

    def __init__(self):
        super().__init__()

    def load_targets(self):
        pass

    def _title(self):
        pass

    def _open_date(self):
        pass

    def _requirements(self):
        pass



jb = JobBullentin()
jb.__dict__


jb.title = 'google-scientist'


jb.schematize()
jb.doc
=======
>>>>>>> 2dc68f9a2380dd4fdebb3bf3aa9d9e2ab98034b9
