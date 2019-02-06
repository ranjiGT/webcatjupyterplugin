# webcatjupyterplugin
A Jupyter Notebook extension for submitting notebook files to Web-CAT.

# Requirement:
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

# Assignment Indentification

The Web-CAT assignment indetification parameters are fetched from the first cell. Paste the following comments in the first cell and change the values with your assignment parameters.

    # Do not edit this cell

    # course: 123
    # a: Assignment 1
    # d: VT
