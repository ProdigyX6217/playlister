from flask import Flask, render_template, request, redirect, url_for
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

@app.route('/playlists/new')
def playlists_new():
    """Create a new playlist."""
    return render_template('playlists_new.html')

@app.route('/playlists', methods=['POST'])
def playlists_submit():
    """Submit a new playlist."""
    # print(request.form.to_dict())
    playlist = {
        'title': request.form.get('title'),
        'description': request.form.get('description')
        'videos': request.form.get('videos').split()
    }
    playlists.insert_one(playlist)
    return redirect(url_for('playlists_index'))

if __name__ == '__main__':
    app.run(debug=True)
