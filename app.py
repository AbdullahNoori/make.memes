from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient()
db = client.meme
memes = db.memes
from flask import Flask, render_template,  request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def memes_index():
    """Show all memes."""
    return render_template('index.html')

@app.route('/memes/new')
def memes_new():
    """Create a new meme."""
    return render_template('new.html')



# Note the methods parameter that explicitly tells the route that this is a POST
@app.route('/memes', methods=['POST'])
def memes_submit():
    """Submit a new meme."""
    # Grab the image urls and make a list out of them
    images = request.form.get('images').split(',')
    # call our helper function to create the list of links
    meme = {
        'title': request.form.get('title'),
        'description': request.form.get('description'),
        'image': request.form.get('image')
    }
    memes.insert_one(meme)
    return redirect(url_for('memes_index'))

@app.route('/memes/<meme_id>')
def memes_show(meme_id):
    """Show a single meme."""
    meme = memes.find_one({'_id': ObjectId(meme_id)})
    return render_template('show.html', meme=meme)

@app.route('/memes/<meme_id>/edit')
def memes_edit(meme_id):
    """Show render meme_edit."""
    meme= memes.find_one({'_id': ObjectId(meme_id)})
    return render_template('edit.html', meme=meme)

@app.route('/memes/<meme_id>', methods=['POST'])
def meme_update(meme_id):
    """Submit an edited meme."""
    # Grab the video IDs and make a list out of them
    images = request.form.get('images').split(',')
    # call our helper function to create the list of links
    meme = {
        'title': request.form.get('title'),
        'description': request.form.get('description'),
        'images': images,
    }

    memes.update_one(
        {'_id': ObjectId(meme_id)},
        {'$set': meme})
    return redirect(url_for('memes_show', meme_id=meme_id))

@app.route('/memes/<meme_id>/delete', methods=['POST'])
def meme_delete(meme_id):
    """Action to delete a comment."""
    memes.delete_one({'_id': ObjectId(meme_id)})
    return redirect(url_for('memes_index'))


if __name__ == '__main__':
    app.run()
