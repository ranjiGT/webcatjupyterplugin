# webcatjupyterplugin
A Jupyter Notebook extension for submitting notebook files to Web-CAT.

# Directions

Make sure that nbextensions is installed on the server:

    pip3 install jupyter_contrib_nbextensions

Download the extension.

    git clone https://github.com/hamzamanzoor/webcatjupyterplugin
    
Once downloaded, you can keep it in sync using regular Git tracking.

Install the extension

    jupyter nbextension install ./webcatjupyterplugin/
    
Enable the extension.

    jupyter nbextension enable webcatjupyterplugin/static/main

# Assignment Indentification

The Web-CAT assignment indetification parameters are fetched from the first cell. Paste the following comments in the first cell and change the values with your assignment parameters.

    # Do not edit this cell

    # course: 123
    # a: Assignment 1
    # d: VT
