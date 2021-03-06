# tutorials
### Files
* start_notebook.py: script to import various libraries and connect to database via SQLAlchemy
* tutorialInit.txt: init file with FeatureWorker parameters
* dlaTutorial.ipynb: jupyter notebook

### Start a notebook
**Step 1**: Connect to the remote server

Log into your remote server and start a screen session:
```bash
screen -R myNotebook
```
**Step 2**: Start the Jupyter server

Before starting the notebook we note that notebook files will be written to the directory from which you are running the notebook. So we will first create a directory called `my_notebooks`, move into that directory and then start the server:
```bash
mkdir my_notebooks && cd "$_"
jupyter notebook --no-browser --port=myportnumber
```
Here `myportnumber` is a free port on the remote machine (for example `8887`). Note if port is already in use on the remote server you will get the follow message (in this example `myportnumber=8887`):
```
> jupyter notebook --no-browser --port=8887
....
[I 09:03:23.972 NotebookApp] The port 8887 is already in use, trying another random port.
[I 09:03:23.975 NotebookApp] Serving notebooks from local directory: /home/sgiorgi
[I 09:03:23.975 NotebookApp] 0 active kernels 
[I 09:03:23.975 NotebookApp] The IPython Notebook is running at: http://localhost:8888/
```
To fix this use `8888` instead of `myportnumber` in the next command. In the last line above the `http://localhost:8888/` is referring to your remote machine. In the next step we will map the remote host / port to your local host /port.

**Step 3**: Map the Jupyter server on the remote machine to your local machine

The general command for this mapping is 
```bash
ssh -i /path/to/privatekey/directory -NL port:localhost:myportnumber username@remote-host-name
```

So on your local machine run (preferably also inside a screen session):
```bash
ssh -i /path/to/public/key -NL 8886:localhost:8888 username@remote-host-name
```

Here `myportnumber` refers to the port on your remote machine (`8888` in this example) and `port` refers to an open port on your local machine (`8886` in this example). There is no reason the two numbers need to be different. You can easily connect port `8888` on your remote machine to port `8888` on your local machine with `... 8888:localhost:8888 ...`

From the `ssh` manual:

```bash
-i identity_file
             Selects a file from which the identity (private key) for public key authentication is read.  The default is ~/.ssh/identity for protocol version 1, and
             ~/.ssh/id_dsa, ~/.ssh/id_ecdsa, ~/.ssh/id_ed25519 and ~/.ssh/id_rsa for protocol version 2.  Identity files may also be specified on a per-host basis in the con‐
             figuration file.  It is possible to have multiple -i options (and multiple identities specified in configuration files).  ssh will also try to load certificate
             information from the filename obtained by appending -cert.pub to identity filenames.
             
-N      Do not execute a remote command.  This is useful for just forwarding ports (protocol version 2 only).
-L [bind_address:]port:host:hostport
             Specifies that the given port on the local (client) host is to be forwarded to the given host and port on the remote side.  This works by allocating a socket to
             listen to port on the local side, optionally bound to the specified bind_address.  Whenever a connection is made to this port, the connection is forwarded over the
             secure channel, and a connection is made to host port hostport from the remote machine.  Port forwardings can also be specified in the configuration file.  IPv6
             addresses can be specified by enclosing the address in square brackets.  Only the superuser can forward privileged ports.  By default, the local port is bound in
             accordance with the GatewayPorts setting.  However, an explicit bind_address may be used to bind the connection to a specific address.  The bind_address of
             “localhost” indicates that the listening port be bound for local use only, while an empty address or ‘*’ indicates that the port should be available from all
             interfaces.
```

**Step 4**: Open the notebook in a web browser

Open a web browser and go to `localhost:port` (in this example `http://localhost:8886`). 



### Resources
Feature Worker
* [Working with FeatureWorker classes](http://dlatk.wwbp.org/tutorials/tut_classes.html)
* [Pandas for WWBP](http://dlatk.wwbp.org/tutorials/tut_pandas.html)
* [Creating an init file with fwInterface](http://dlatk.wwbp.org/tutorials/tut_ini_files.html)

Other
* [Seaborn: statistical data visualization](https://stanford.edu/~mwaskom/software/seaborn/)

