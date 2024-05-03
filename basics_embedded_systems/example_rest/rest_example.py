from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop

class HelloHandler(RequestHandler):
    def get(self):
        self.write({'message': 'hello world'})


def make_app():
    urls = [("/", HelloHandler)]
    return Application(urls)


if __name__ == '__main__':
    app = make_app()
    app.listen(3000)
    IOLoop.instance().start()
