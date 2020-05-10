from flask import Flask           
import socket
app = Flask(__name__)             

@app.route("/")                   
def hello():                      
    return "I am on "+ socket.gethostname()         
if __name__ == "__main__":        
    app.run()                     