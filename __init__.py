from Web-CAT-Jupyter-Plugin.handlers import setup_handlers
# Jupyter Extension points
def _jupyter_server_extension_paths():
    return [{
        'module': 'Web-CAT-Jupyter-Plugin',
    }]

def _jupyter_nbextension_paths():
    return [{
        "section": "notebook",
        "dest": "Web-CAT-Jupyter-Plugin",
        "src": "static",
        "require": "Web-CAT-Jupyter-Plugin/main"
    }]

def load_jupyter_server_extension(nbapp):
    setup_handlers(nbapp.web_app)