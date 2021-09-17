from django.contrib.auth.forms import UserCreationForm,forms
from django.contrib.auth.models import User



class UserCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #htmlの表示を変更可能にします
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

    class Meta:
       model = User
       fields = ("username", "password1", "password2",)

"""
class UserDetailForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #htmlの表示を変更可能にします
        self.fields['grade'].widget.attrs['class'] = 'form-control'
        self.fields['schoolId'].widget.attrs['class'] = 'form-control'
        self.fields['position'].widget.attrs['class'] = 'form-control'

    CHOICE = [
        ("0","プレイヤー"),
        ("1","マネージャー"),
        ("2","コーチ"),
        ("3","OB"),
    ]

    grade = forms.IntegerField()
    schoolId = forms.IntegerField()
    position = forms.ChoiceField(
        label="役職" ,
        required=True, 
        choices=CHOICE,
        widget = forms.RadioSelect(),
        )

    class Meta:
        model = UserDetail
        fields = ("grade","schoolId", "position")
    
        labels = {
            "grade":"学年",
            "id":"学内ID",
            "position":"役職"
        }
        help_text = {

        }
    """