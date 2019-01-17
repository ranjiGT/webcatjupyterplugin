from webcatjupyterplugin.handlers import setup_handlers
# Jupyter Extension points
def _jupyter_server_extension_paths():
    return [{
        'module': 'webcatjupyterplugin',
    }]

def _jupyter_nbextension_paths():
    return [{
        "section": "notebook",
        "dest": "webcatjupyterplugin",
        "src": "static",
        "require": "webcatjupyterplugin/main"
    }]

def load_jupyter_server_extension(nbapp):
    setup_handlers(nbapp.web_app)