
import setuptools

setuptools.setup(
    name="webcatjupyterplugin",
    version='0.1.0',
    url="https://github.com/ranjiGT/webcatjupyterplugin",
    author="Ranji Raj",
    description="Jupyter Notebook Plugin for submitting files to Web-CAT",
    packages=setuptools.find_packages(),
    install_requires=[
        'notebook',
        'jupyterhub',
        'bs4',
        'gitpython',
        'requests'
    ],
    package_data={'webcatjupyterplugin': ['static/*']},
)
