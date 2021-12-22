####################### Changes in jupyter config ###########################
if [ ! -f ~/.jupyterhub_config.py ]; then
   jupyterhub --generate-config
fi

echo 'c.NotebookApp.disable_check_xsrf = True' >> ~/.jupyterhub_config.py
