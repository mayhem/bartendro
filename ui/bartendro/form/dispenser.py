#!/usr/bin/env python
from wtforms import Form, SelectField, SubmitField


class DispenserForm(Form):

    save = SubmitField("save")
    cancel = SubmitField("cancel")


form = DispenserForm()
