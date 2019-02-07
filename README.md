# webcatjupyterplugin
A Jupyter Notebook extension for submitting notebook files to Web-CAT.

# Requirements

1. Python 3
2. pip
3. Jupyter Notebook

# Directions

## Linux / macOS

##### With Anaconda:
Follow these steps if you are running Jupyter Notebooks through Anaconda:

1. conda install git pip
2. pip install git+https://github.com/CSSPLICE/webcatjupyterplugin
3. jupyter serverextension enable --py webcatjupyterplugin
4. jupyter nbextension install --py webcatjupyterplugin
5. jupyter nbextension enable --py webcatjupyterplugin
7. Download the file env.sh or clone the repository and run the command below
8. sh env.sh

You can skip the 7<sup>th</sup> and 8<sup>th</sup> steps and manually run the following commands:
1. jupyter notebook --generate-config
2. Add the following line at the end of ~/.jupyter/jupyter_notebook_config.py
    - c.NotebookApp.disable_check_xsrf = True 
    
##### With pip:

If you are not using Anaconda, use the following commands:

1. pip3 install git+https://github.com/CSSPLICE/webcatjupyterplugin
2. jupyter serverextension enable --py webcatjupyterplugin
3. jupyter nbextension install --py webcatjupyterplugin
4. jupyter nbextension enable --py webcatjupyterplugin
5. Download the file env.sh or clone the repository and run the command below
6. sh env.sh


You can skip the 5<sup>th</sup> and 6<sup>th</sup> steps and manually run the following commands:
1. jupyter notebook --generate-config
2. Add the following line at the end of ~/.jupyter/jupyter_notebook_config.py
    - c.NotebookApp.disable_check_xsrf = True 
    
## Windows

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


# Screenshots

#### Submit to Web-CAT button
!["Submit to Web-CAT button"](screens/submit_button.png "Submit to Web-CAT button")


#### Web-CAT Assignment Parameters
!["Web-CAT Assignment Parameters"](screens/assignment_parameters.png "Web-CAT Assignment Parameters")


#### Assignment Submission
!["Assignment Submission"](screens/submission.png "Assignment Submission")
