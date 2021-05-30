from wsgiref.simple_server import make_server
import falcon


class Resource:

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_TEXT
        resp.text = 'this is an docker example'


resource = Resource()
app = falcon.App()
app.add_route('/example', resource)

if __name__ == '__main__':
    with make_server('', 80, app) as httpd:
        httpd.serve_forever()
