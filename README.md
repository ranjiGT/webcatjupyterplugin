# webcatjupyterplugin
A Jupyter Notebook extension for submitting notebook files to Web-CAT.

# Requirements

1. Python 3
2. pip
3. Jupyter Notebook

# Directions

Make sure that nbextensions is installed on the server:

    pip3 install jupyter_contrib_nbextensions

You can install this directly from git:

    pip3 install git+https://github.com/CSSPLICE/webcatjupyterplugin
    jupyter serverextension enable --py webcatjupyterplugin
    jupyter nbextension install --py webcatjupyterplugin
    
To enable this extension for all notebooks:

    jupyter nbextension enable --py webcatjupyterplugin
    
Run the commands in env.sh file

# Windows

If you have Windows operating system, follow these steps:

1. Install Anaconda
2. Open Anaconda Prompt and run these commands:
3. conda install git pip
4. pip install git+https://github.com/CSSPLICE/webcatjupyterplugin
5. jupyter serverextension enable --py webcatjupyterplugin
6. jupyter nbextension install --py webcatjupyterplugin
7. jupyter nbextension enable --py webcatjupyterplugin
8. jupyter notebook --generate-config

This will generate a default config file and you will get the output like "Writing default config to: C:\Users\UserName\\.jupyter\jupyter_notebook_config.py"

Run the following command but make sure to change the path to the ones returned by the above command

9. echo c.NotebookApp.disable_check_xsrf = True >> C:\Users\UserName\\.jupyter\jupyter_notebook_config.py



# Assignment Indentification

The Web-CAT assignment indetification parameters are fetched from the first cell. Paste the following comments in the first cell and change the values with your assignment parameters.

    # Do not edit this cell

    # course: 123
    # a: Assignment 1
    # d: VT
