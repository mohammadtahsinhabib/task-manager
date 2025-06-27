from django import forms


class TaskForm(forms.Form):
    title=forms.CharField(label="Task Title")
    descriptions=forms.CharField(widget=forms.Textarea,label="Task Descriptions")
    due_date = forms.DateField(widget=forms.SelectDateWidget, label="Due Date")
    assigned_to = forms.MultipleChoiceField(
    widget=forms.CheckboxSelectMultiple, choices=[], label='Assigned To')
    
    def __init__(self, *args, **kwargs):
        employees = kwargs.pop("employees", [])
        super().__init__(*args, **kwargs)
        self.fields['assigned_to'].choices = [(emp.id, emp.name) for emp in employees]

    
