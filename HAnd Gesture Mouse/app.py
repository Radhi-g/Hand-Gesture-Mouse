from flask import Flask, render_template, Response
import os
app = Flask(__name__)    
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/mouse')
def virtual_mouse():
    return render_template('mouse.html')


@app.route('/video_feed')
def video_feed():
    return Response(virtualMouse.gen(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(debug=True)

