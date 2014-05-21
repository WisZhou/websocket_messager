#!/usr/bin/python
#encoding=utf-8
#auther: wiszhou
#data: 2013.10.24
'''Provide a websocket interface and a http interface.
Messages posted to http interface would be receive by browser who connect to
the websocket interface.
'''
import utils
import config


import tornado.web
import tornado.ioloop
import tornado.websocket
import tornado.httpserver
from tornado.options import define, options 

define("port", default=8100, help="run on the given port", type=int) 
define("host", default='0.0.0.0', help="bind ip", type=str) 
LOGGER = utils.COMMON_LOGGER

all_websocket = []

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('websocekt server ok')

class MSGHandler(tornado.web.RequestHandler):
    def post(self):
        msg = self.get_argument('msg', strip=True)
        LOGGER.debug(msg)
        for websocket in all_websocket:
            websocket.write_message(msg)

class ExampleHandler(tornado.web.RequestHandler):
    '''Open this page on Chrome and try to post some msg on MSGHandler
        Both plain text and html ok
    '''
    def get(self):
        self.write('''
            <html>
                <body>
                    <div id="info" style="font-weight: bold;"></div>
                    <span>
                        Server say:
                    </span>
                    <div id="output" style="margin-left: 20px;
                    border: dotted 1px #aaa;
                    display: inline-block;
                    vertical-align: middle;
                    padding: 20px;"></div>
                </body>
                <foot>
                    <script src="http://code.jquery.com/jquery-1.11.0.min.js" type="text/javascript"></script>
                    <script type="text/javascript">
                        var ws = new WebSocket('%s');
                        ws.onopen = function(){
                            $('#info').css('color', 'green').html("Connect to websocket server success.");
                        };
                        ws.onmessage = function(msg){
                            $('#output').html(msg.data);
                        };
                        ws.onclose = function(){
                            $('#info').css('color', 'red').html("Cannot connect to websocket server! Please ensure your config of WEBSOCKET_HOST and WEBSOCKET_PORT.");
                        };
                    </script>
                </foot>
            </html>
        ''' % config.WEBSOCKET_URL)

class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        all_websocket.append(self)
        LOGGER.debug('connection opened... Connections: %d' % len(all_websocket))

    def on_message(self, message):
        for websocket in all_websocket:
            websocket.write_message(message)

    def on_close(self):
        try:
           all_websocket.remove(self)
        except ValueError:
            LOGGER.warning('Websocket instans is missed in manager.')
        LOGGER.debug('connection closed... Connections: %d' % len(all_websocket))

application = tornado.web.Application([
    (r'/ws', WSHandler),
    (r'/msg', MSGHandler),
    (r'/example', ExampleHandler),
    (r'/', MainHandler),
])

if __name__ == "__main__":
    options.parse_command_line()
    port = options.port
    host = options.host 
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(port, host)
    print 'Listen on %s:%s OK!'% (host, port)
    tornado.ioloop.IOLoop.instance().start()
