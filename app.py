# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

from flask import Flask, render_template
# from sqlalchemy import true
from flask import Flask
from final_flask import app
if __name__=='__main__':
    app.run(debug=True)