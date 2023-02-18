#!/usr/bin/env python
from wtforms import Form, StringField, DecimalField, HiddenField, validators, TextAreaField, SubmitField, BooleanField

MAX_SUGGESTED_DRINK_SIZE = 5000 # in ml

class DrinkForm(Form):
    id = HiddenField("id", default=0)
    drink_name = StringField("Name", [validators.Length(min=3, max=255)])
    desc = TextAreaField("Description", [validators.Length(min=3, max=1024)])
    popular = BooleanField("List this drink in the <i>the essentials</i> section.")
    available = BooleanField("List this drink in the main menu")
    save = SubmitField("save")
    cancel = SubmitField("cancel")

form = DrinkForm()
