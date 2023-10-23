from django import forms
 
class SelectTestForm(forms.Form):
  SELVALUE = (
    ('标题', 'first'),
    ('内容', 'second'),
    ('作者', 'third'),
  )
  sel_value = forms.CharField(max_length=10,widget=forms.widgets.Select(choices=SELVALUE))