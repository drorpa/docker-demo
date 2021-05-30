from wsgiref.simple_server import make_server
import falcon
import pandas as pd

class Resource:

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_TEXT
        myinput = req.params.get('input')
        df = pd.DataFrame({'input': [myinput]})
        df.to_csv('/code/data/df.csv')
        resp.text = f'this is an docker example, got input: {myinput}'


resource = Resource()
app = falcon.App()
app.add_route('/example', resource)

if __name__ == '__main__':
    with make_server('', 80, app) as httpd:
        httpd.serve_forever()
