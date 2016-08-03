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
* Start the notebook
```bash
jupyter notebook --no-browser
```
* On your local machine run
```bash
ssh -i /path/to/public/key -NL 8157:localhost:8888 username@venti-host-name
```

### Resources
Feature Worker
* [Working with FeatureWorker classes](http://wiki.wwbp.org/pmwiki.php/Tutorials/WorkingWithClasses)
* [Pandas for WWBP](http://wiki.wwbp.org/pmwiki.php/Tutorials/PandasForWWBP)
* [Loading variables from a file](http://wiki.wwbp.org/pmwiki.php/FwInterfaceDocumentation/FromFile)
* [Creating an init file with fwInterface](http://wiki.wwbp.org/pmwiki.php/FwInterfaceDocumentation/ToFile)

Other
* [Seaborn: statistical data visualization](https://stanford.edu/~mwaskom/software/seaborn/)

