from notebook.utils import url_path_join as ujoin
from notebook.base.handlers import IPythonHandler
import os, json, git, urllib, requests
from bs4 import BeautifulSoup

class WebCatPushHandler(IPythonHandler):

    def error_and_return(self, dirname, reason):

        # send error
        self.send_error(500, reason=reason)

        # return to directory
        os.chdir(dirname)

    def put(self):

        # obtain filename and msg for commit
        data = json.loads(self.request.body.decode('utf-8'))
        filename = urllib.parse.unquote(data['filename'])

        # get current directory (to return later)
        cwd = os.getcwd()
   
    
        payload = {
            'course': "123",
            'a': "Inst Assignment X",
            'd': "VT"
            };
        url = 'https://web-cat.cs.vt.edu/Web-CAT/WebObjects/Web-CAT.woa/wa/submit'

        filepath = cwd+"/"+filename

        files = {'file1': open(filepath, 'rb')}
        redirectLink = ""
        try:
            response = requests.post(url, data=payload, files=files)
            soup = BeautifulSoup(response.content, "html.parser")
            for link in soup.findAll('a'):
                redirectLink=link.get('href')
        except Exception as e:
            print("Error")
            print(e)
            self.error_and_return(cwd, "Could send request to",e)
            return

        # return to directory
        os.chdir(cwd)

        # close connection
        self.write(json.dumps({'status': 200, 'statusText': cwd+"/"+filename, 'responseText': response.content.decode("utf-8"), 'redirectLink': redirectLink}))


def setup_handlers(nbapp):
    route_pattern = ujoin(nbapp.settings['base_url'], '/webcat/push')
    nbapp.add_handlers('.*', [(route_pattern, WebCatPushHandler)])
