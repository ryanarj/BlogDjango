from django import forms

BIRTH_YEAR_CHOICES = ('1990', '1991', '1992', '1993')
FAVORITE_COLORS_CHOICES = (
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
)

class SimpleForm(forms.Form):
	YEARS = [10, 20 , 30]
	birth_year = forms.DateField(required=True, widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
	favorite_colors = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, choices=FAVORITE_COLORS_CHOICES)