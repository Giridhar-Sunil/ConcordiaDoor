from django import forms

class CourseSearchForm(forms.Form):
    course_code = forms.CharField(label='Course Code', max_length=10)
