import http.client

host = input("Host/IP: ")
port = input("Port(default:80): ")
resrc = input("URL: ")

if(port == ""):
    port = 80

try:
    conn = http.client.HTTPConnection(host, port)
    conn.request("GET", "/" + resrc)
    resp = conn.getresponse()
    print(resp.status, resp.reason)
    conn.close()
except ConnectionRefusedError:
    print("Connection failed")
