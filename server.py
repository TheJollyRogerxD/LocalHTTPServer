import http.server
import socketserver

port = 1337
Handler = http.server.SimpleHTTPRequestHandler
Handler.extensions_map.update({
    '.webapp': 'application/x-web-app-manifest+json'
})
http = socketserver.TCPServer(("", port), Handler)

print("Starting server at port: " + str(port))
http.serve_forever()
