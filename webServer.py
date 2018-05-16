from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi

#Request handler class
class webserverHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith("/hello"): #path - this is a variable provided by the BaseHTTPRequestHandler class, this contains the URL sent by the client to server
                self.send_response(200)
                self.send_header('Content_type', 'text/html')
                self.end_headers()

                output = ""
                output += "<html><body>Hello!"
                output += """<form method = 'POST' enctype='multipart/form-data' action='/hello'>
                <h2>What would you like me to say?</h2><input name = 'message'
                type = 'text'><input type = 'submit'></form>"""
                output += "</body></html>"
                
                self.wfile.write(output) # this writes the message back to client
                print output
                return

            if self.path.endswith("/hola"):
                self.send_response(200)
                self.send_header('Content_type', 'text/html')
                self.end_headers()

                output = ""
                output += "<html><body>Hola!<a href = '/hello'>Go back to hello</a>"
                output += """<form method = 'POST' enctype='multipart/form-data' action='/hello'>
                <h2>What would you like me to say?</h2><input name = 'message'
                type = 'text'><input type = 'submit'></form>"""
                output += "</body></html>"
                 
                self.wfile.write(output) # this writes the message back to client
                print output
                return
            
        except IOError:
            self.send_error(404, "File Not Found %s" %self.path)

    def do_POST(self):
        try:
            self.send_response(301)
            self.end_headers()

            ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
            if ctype == 'multipart/form-data':
                fields=cgi.parse_multipart(self.rfile, pdict)
                messagecontent = fields.get('message')

            output = ""
            output += "<html><body>"
            output += " <h2> Okay, how about this: </h2>"
            output += "<h1> %s </h1>" % messagecontent[0]

            output += """<form method = 'POST' enctype='multipart/form-data' action='/hello'>
                <h2>What would you like me to say?</h2><input name = 'message'
                type = 'text'><input type = 'submit'></form>"""
            output += "</body></html>"
            self.wfile.write(output)
            print output
            
        except IOError:
            self.send_error(404, "File Not Found %s" %self.path)
   
#entry point of code
def main():
    try:
        #create an instance of the HTTP Server class
        port = 8080
        server = HTTPServer(('',port),webserverHandler)
        #see documentation of HTTPServer class
        #class http.server.HTTPServer(server_address, RequestHandlerClass)
        #server_address if a tuple, (host name, port number)
        #have left the host name blank and theport number is set to 8080
        #webserverHandler is the handler class that needs tobe defined
        
        print "Web serverrunning onport %s" %port
        server.serve_forever()

    except KeyboardInterrupt:
        #this interruptkeyboard interrupt is the builtin exception on python, when user holds ctrl+c
        print "^C entered, stopping web server..."
        Server.socket.close()


# the following code should be written at the End of file
# This is added to immediately run the main menthod, when the python interpreter executes the script

if __name__ == '__main__':
    main()
    
