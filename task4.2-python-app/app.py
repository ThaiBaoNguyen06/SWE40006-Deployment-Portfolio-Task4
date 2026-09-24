from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>SWE40006 Docker Deployment</h1>
    <p>Hi, I am Thai. This is Python web application is running inside Docker container</p> 
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)