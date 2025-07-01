from django import forms
from django.forms import ChoiceField

from obs_system_app.models import Courses, SessionYearModel, Subjects, Students

class ChoiceNoValidation(ChoiceField):
    def validate(self, value):
        pass

class DateInput(forms.DateInput):
    input_type = "date"

class AddStudentForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class": "form-control", "autocomplete": "off"}))
    password = forms.CharField(label="Password", max_length=50, widget=forms.PasswordInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(label="First Name", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(label="Last Name", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(attrs={"class": "form-control", "autocomplete": "off"}))
    address = forms.CharField(label="Address", max_length=255, widget=forms.TextInput(attrs={"class": "form-control"}))
    date_of_birth = forms.DateField(label="Date of Birth", widget=DateInput(attrs={"class": "form-control"}))
    
    enrollment_date = forms.DateField(label="Enrollment Date", widget=DateInput(attrs={"class": "form-control"}))
    expected_graduation_date = forms.DateField(label="Expected Graduation Date", widget=DateInput(attrs={"class": "form-control"}))

    course = forms.ChoiceField(label="Faculty", choices=[], widget=forms.Select(attrs={"class": "form-control"}))
    sex = forms.ChoiceField(label="Sex", choices=[("Male", "Male"), ("Female", "Female")], widget=forms.Select(attrs={"class": "form-control"}))
    session_year_id = forms.ChoiceField(label="Session Year", choices=[], widget=forms.Select(attrs={"class": "form-control"}))
    profile_pic = forms.FileField(label="Profile Picture", max_length=50, widget=forms.FileInput(attrs={"class": "form-control"}))

    def __init__(self, *args, **kwargs):
        super(AddStudentForm, self).__init__(*args, **kwargs)

        # Dynamic loading of Courses
        course_choices = []
        try:
            courses = Courses.objects.all()
            for course in courses:
                course_choices.append((course.id, course.course_name))
        except:
            pass
        self.fields['course'].choices = course_choices

        session_choices = []
        try:
            sessions = SessionYearModel.object.all()
            for session in sessions:
                session_choices.append((session.id, f"{session.session_start_year} TO {session.session_end_year}"))
        except:
            pass
        self.fields['session_year_id'].choices = session_choices
class EditStudentForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(label="First Name", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(label="Last Name", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    address = forms.CharField(label="Address", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    date_of_birth = forms.DateField(label="Date of Birth", widget=DateInput(attrs={"class": "form-control"}))

    enrollment_date = forms.DateField(label="Enrollment Date", widget=DateInput(attrs={"class": "form-control"}))
    expected_graduation_date = forms.DateField(label="Expected Graduation Date", widget=DateInput(attrs={"class": "form-control"}))

    course_list = []
    try:
        courses = Courses.objects.all()
        for course in courses:
            small_course = (course.id, course.course_name)
            course_list.append(small_course)
    except:
        course_list = []

    session_list = []
    try:
        sessions = SessionYearModel.object.all()
        for ses in sessions:
            small_ses = (ses.id, str(ses.session_start_year) + " TO " + str(ses.session_end_year))
            session_list.append(small_ses)
    except:
        pass

    gender_choice = (
        ("Male", "Male"),
        ("Female", "Female")
    )

    course = forms.ChoiceField(label="Course", choices=course_list, widget=forms.Select(attrs={"class": "form-control"}))
    sex = forms.ChoiceField(label="Sex", choices=gender_choice, widget=forms.Select(attrs={"class": "form-control"}))
    session_year_id = forms.ChoiceField(label="Session Year", choices=session_list, widget=forms.Select(attrs={"class": "form-control"}))
    profile_pic = forms.FileField(label="Profile Pic", max_length=50, widget=forms.FileInput(attrs={"class": "form-control"}), required=False)

class EditResultForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.staff_id = kwargs.pop("staff_id")
        super(EditResultForm, self).__init__(*args, **kwargs)
        subject_list = []
        try:
            subjects = Subjects.objects.filter(staff_id=self.staff_id)
            for subject in subjects:
                subject_single = (subject.id, subject.subject_name)
                subject_list.append(subject_single)
        except:
            subject_list = []
        self.fields['subject_id'].choices = subject_list

    session_list = []
    try:
        sessions = SessionYearModel.object.all()
        for session in sessions:
            session_single = (session.id, str(session.session_start_year) + " TO " + str(session.session_end_year))
            session_list.append(session_single)
    except:
        session_list = []

    subject_id = forms.ChoiceField(label="Subject", widget=forms.Select(attrs={"class": "form-control"}))
    session_ids = forms.ChoiceField(label="Session Year", choices=session_list, widget=forms.Select(attrs={"class": "form-control"}))
    student_ids = ChoiceNoValidation(label="Student", widget=forms.Select(attrs={"class": "form-control"}))
    assignment_marks = forms.CharField(label="Assignment Marks", widget=forms.TextInput(attrs={"class": "form-control"}))
    exam_marks = forms.CharField(label="Exam Marks", widget=forms.TextInput(attrs={"class": "form-control"}))
