# tutorials
### Files
* start_notebook.py: script to import various libraries and connect to database via SQLAlchemy
* tutorialInit.txt: init file with FeatureWorker parameters
* dlaTutorial.ipynb: jupyter notebook

### Start a notebook
* Log into venti and start a screen session:
```bash
screen -R myNotebook
```
* Start the notebook. The directory where you run this line will be your home directory in your notebook.
```bash
jupyter notebook --no-browser --port=myportnumber
```
Note if port is already in use on venti you will get the follow message (where `myportnumber=8887`):
```
[I 09:03:23.972 NotebookApp] The port 8887 is already in use, trying another random port.
[I 09:03:23.975 NotebookApp] Serving notebooks from local directory: /home/sgiorgi
[I 09:03:23.975 NotebookApp] 0 active kernels 
[I 09:03:23.975 NotebookApp] The IPython Notebook is running at: http://localhost:8888/
```
To fix this use `8888` instead of `myportnumber` in the next command.

* On your local machine run (preferably also inside a screen session):
```bash
ssh -i /path/to/public/key -NL port:localhost:myportnumber username@venti-host-name
```
* Open a web browser and go to localhost:port



### Resources
Feature Worker
* [Working with FeatureWorker classes](http://wiki.wwbp.org/pmwiki.php/Tutorials/WorkingWithClasses)
* [Pandas for WWBP](http://wiki.wwbp.org/pmwiki.php/Tutorials/PandasForWWBP)
* [Loading variables from a file](http://wiki.wwbp.org/pmwiki.php/FwInterfaceDocumentation/FromFile)
* [Creating an init file with fwInterface](http://wiki.wwbp.org/pmwiki.php/FwInterfaceDocumentation/ToFile)

Other
* [Seaborn: statistical data visualization](https://stanford.edu/~mwaskom/software/seaborn/)

