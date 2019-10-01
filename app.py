from flask import Flask, render_template
from pymongo import MongoClient

client = MongoClient()
db = client.Playlister
playlists = db.playlists
app = Flask(__name__)

# @app.route('/')
# def index():
#     """Return homepage"""
#     return render_template('home.html', msg='Flask is Cool!!')


# OUR MOCK ARRAY OF PROJECTS
# playlists = [
#     { 'title': 'Dogs Videos', 'description': 'Dogs acting weird' },
#     { 'title': '90\'s Music', 'description': 'I Get Around!' }
# ]

@app.route('/')
def playlists_index():
    """Show all playlists."""
    return render_template('playlists_index.html', playlists=playlists.find())

if __name__ == '__main__':
    app.run(debug=True)
