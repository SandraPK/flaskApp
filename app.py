from flask import Flask

app=Flask(__name__)

@app.route("/")
def hello_word():
    print("hello")
    var="hello word"
    return var

if __name__=="__main__":
    app.run(debug=True)
    