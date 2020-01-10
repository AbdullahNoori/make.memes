from unittest import TestCase, main as unittest_main, mock
from app import app
from bson.objectid import ObjectId

sample_meme_id = ObjectId('5d55cffc4a3d4031f42827a3')
sample_meme = {
    'title': 'meme Videos',
    'description': 'meme is so fun! ',
    'videos': [
        'https://youtube.com/embed/hY7m5jjJ9mM',
        'https://www.youtube.com/embed/CQ85sUNBK7w'
    ]
}
sample_form_data = {
    'title': sample_meme['title'],
    'description': sample_meme['description'],
    'videos': '\n'.join(sample_meme['videos'])
}

class memesTests(TestCase):
    """Flask tests."""

    def setUp(self):
        """Stuff to do before every test."""

        # Get the Flask test client
        self.client = app.test_client()

        # Show Flask errors that happen during tests
        app.config['TESTING'] = True

    def test_index(self):
        """Test the memes homepage."""
        result = self.client.get('/')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'meme', result.data)

    def test_new(self):
        """Test the new meme creation page."""
        result = self.client.get('/memes/new')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'New meme', result.data)
    
    @mock.patch('pymongo.collection.Collection.find_one')
    def test_show_meme(self, mock_find):
        """Test showing a single meme."""
        mock_find.return_value = sample_meme

        result = self.client.get(f'/memes/{sample_meme_id}')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'meme Videos', result.data)

    @mock.patch('pymongo.collection.Collection.find_one')
    def test_edit_meme(self, mock_find):
        """Test editing a single meme."""
        mock_find.return_value = sample_meme

        result = self.client.get(f'/memes/{sample_meme_id}/edit')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'meme Videos', result.data)
    
    @mock.patch('pymongo.collection.Collection.insert_one')
    def test_submit_meme(self, mock_insert):
        """Test submitting a new meme."""
        result = self.client.post('/memes', data=sample_form_data)

        # After submitting, should redirect to that meme's page
        self.assertEqual(result.status, '302 FOUND')
        mock_insert.assert_called_with(sample_meme)

    @mock.patch('pymongo.collection.Collection.update_one')
    def test_update_meme(self, mock_update):
        result = self.client.post(f'/memes/{sample_meme_id}/update', data=sample_form_data)

        self.assertEqual(result.status, '302 FOUND')
        mock_update.assert_called_with({'_id': sample_meme_id}, {'$set': sample_meme})

    @mock.patch('pymongo.collection.Collection.delete_one')
    def test_delete_meme(self, mock_delete):
        form_data = {'_method': 'DELETE'}
        result = self.client.post(f'/memes/{sample_meme_id}/delete', data=form_data)
        self.assertEqual(result.status, '302 FOUND')
        mock_delete.assert_called_with({'_id': sample_meme_id})

if __name__ == '__main__':
    unittest_main()
