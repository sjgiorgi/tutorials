def isnotebook():
    try:
        shell = get_ipython().__class__.__name__
        if shell == 'ZMQInteractiveShell':
            c = get_config()
            c.InteractiveShellApp.matplotlib = "inline"
            return True   # Jupyter notebook or qtconsole
        elif shell == 'TerminalInteractiveShell':
            mpl.use('Agg')
            return False  # Terminal running IPython
        else:
            return False  # Other type (?)
    except NameError:
        mpl.use('Agg')
        return False      # Probably standard Python interpreter


# infrastructure
print("Importing FeatureStar, FeatureGetter and OutcomeGetter...")
print("mif and mm...")
import sys
if sys.version_info[0] < 3:
    print("Python 2")
    sys.path.append("/home/sgiorgi/code/python2/")
else:
    print("Python 3")
    sys.path.append("/home/sgiorgi/code/python3/")

from dlatk.featureStar import FeatureStar
from dlatk.mysqlMethods import mysql_iter_funcs as mif
from dlatk.mysqlMethods import mysqlMethods as mm

# pandas
print("pandas as pd...")
import pandas as pd
pd.set_option('display.width', 200)
pd.set_option('display.max_colwidth',100)

# numpy
print("numpy as np...")
import numpy as np

# matplotlib
print("matplotlib as mpl...")
import matplotlib as mpl
isnotebook()
import matplotlib.pyplot as plt
print("pyplot as plt...")

# other
try:
    import seaborn as sns
    print("seaborn as sns...")
except:
    print("Cannot import seaborn")

try:
    import mpld3
    print("mpld3...")
except:
    print("Cannot import mpld3")

try:
    import bokeh
    print("bokeh...")
except:
    print("Cannot import bokeh")

host = None
# get db
if len(sys.argv)==1 or len(sys.argv) > 3:
    if sys.version_info[0] < 3:
        db = raw_input('Start sqlalchemy engine for database (or hit Enter for None): ')
    else:
        db = input('Start sqlalchemy engine for database (or hit Enter for None): ')
elif len(sys.argv)==2:
    db = sys.argv[1]
    host = "wwbp-venti"
elif len(sys.argv)==3:
    db = sys.argv[1]
    host = "wwbp-grande"

if db:
    db_eng = mif.get_db_engine(db, host)
    print("")
    print("Engine initialized with varname 'db_eng'")
    print("")
else:
    print("")
    print("No engine initialized. Initialize with:")
    print("> db_eng = mif.get_db_engine(db)")
    print("")

