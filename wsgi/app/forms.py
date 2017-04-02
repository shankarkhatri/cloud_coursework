from flask_wtf import Form
from wtforms import TextField, validators

class MessageForm(Form):
   message = TextField(u'This app shows 3 different sentiment analysis , by taking in user input!', [validators.optional(), validators.length(max=200)])
