
import tornado.ioloop
import tornado.web


def serve(parser, run_function):
    """ Serve argparse parser and run function with parsed args """
    app = tornado.web.Application([
        (r"/", MainHandler, dict(
            argument_parser=parser, run_function=run_function)),
    ])
    app.listen(8889)
    tornado.ioloop.IOLoop.current().start()


class MainHandler(tornado.web.RequestHandler):
    def initialize(self, argument_parser, run_function):
        self.argument_parser = argument_parser
        self.run_function = run_function

    def get(self):
        title = self.argument_parser.description
        actions = self.argument_parser._actions
        self.render('argserve.html', title=title, actions=actions)

    def post(self):
        pass


class MyActionModule(tornado.web.UIModule):
    pass
