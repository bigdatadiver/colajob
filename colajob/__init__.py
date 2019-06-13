
import __future__
print(f"\n __future__.division : {__future__.division}")
import os
print(f"\n os.path.abspath(__file__) :\n{os.path.abspath(__file__)}")
print(f"\n os.path.dirname(os.path.abspath(__file__)) :\n{os.path.dirname(os.path.abspath(__file__))}")
PKG_PATH = os.path.dirname(os.path.abspath(__file__))
print(f"\n os.path.dirname(os.path.dirname(os.path.abspath(__file__))) :\n{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}")
PJT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
<<<<<<< HEAD
DATA_PATH = f"{PJT_PATH}/dataset"
=======
>>>>>>> 2dc68f9a2380dd4fdebb3bf3aa9d9e2ab98034b9
