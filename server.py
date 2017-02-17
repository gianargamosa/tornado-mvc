import json
import traceback
from tornado import web, options, ioloop

class MyAppBaseHandler(web.RequestHandler):
    def write_error(self, status_code, **kwargs):
        self.set_header('Content-Type', 'application/json')
        if self.settings.get("serve_traceback") and "exc_info" in kwargs:
            # in debug mode, try to send a traceback
            lines = []
            for line in traceback.format_exception(*kwargs["exc_info"]):
                lines.append(line)
            self.write(json.dumps({
                'error': {
                    'code': status_code,
                    'message': self._reason,
                    'traceback': lines,
                }
            }))
        else:
            self.write(json.dumps({
                'error': {
                    'code': status_code,
                    'message': self._reason,
                }
            }))


class AgeHandler(MyAppBaseHandler):

    def get(self):
        age = self.get_argument('age')
        age = int(age)
        # if age < 1 or age > 200:
            # raise MyAppException(reason='Wrong age value.', status_code=400)
        self.write('Your age is {age}'.format(age=age))


class MyApplication(web.Application):
    def __init__(self, **kwargs):
        kwargs['handlers'] = [
            web.url(r'/', AgeHandler, name='age'),
        ]
        kwargs['debug'] = True
        super(MyApplication, self).__init__(**kwargs)


if __name__ == '__main__':
    options.parse_command_line()
    application = MyApplication()
    application.listen(5000)
    ioloop.IOLoop.instance().start()