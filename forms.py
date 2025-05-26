from wtforms import Form, StringField, SubmitField, validators

class ExtractForms (Form):
    product_id = StringField("Product id", name="product_id", id = "product_id" validators=[
        validators.Datarequiered(message),
        validators.Length(min= 6, max =10, message = "product id should have between 6 and 10 characters"),
        validators.Regex(r'[0-9],*',message = "Product id can contain only digits")
    ])
    submit = SubmitField("Extrac opinions")
















