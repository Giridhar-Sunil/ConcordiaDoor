from django.shortcuts import render, redirect
from .models import Textbook
from .forms import CourseSearchForm

def search_textbooks(request):
    form = CourseSearchForm()
    if request.method == "GET":
        return render(request, 'search_coursecode.html', {'form': form})
    elif request.method == "POST":
        form = CourseSearchForm(request.POST)
        if form.is_valid():
            course_code = form.cleaned_data['course_code']
            course_code = course_code.replace(" ", "")
        return redirect(f'/textbooks/{course_code}/')   

def display_textbooks(request, course_code):
    textbooks = Textbook.objects.filter(course_code=course_code, availability=True)
    return render(request, 'listbook.html', {'textbooks': textbooks, 'course_code':course_code})