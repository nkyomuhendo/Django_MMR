from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Product, Category, Exercise

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs) 

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'

    
class AddProductForm(forms.ModelForm):
    
    def __init__(self, created_by, *args, **kwargs):
        super(AddProductForm, self).__init__(*args, **kwargs)
        self.fields['category'] = forms.ModelChoiceField(queryset=Category.objects.all())
        # self.fields['created_by'] = forms.(request.user())
 
    title = forms.CharField(max_length=255)
    description = forms.CharField(max_length=255)
    table = forms.IntegerField()
    no_of_samples = forms.IntegerField() 
    low_test_mark = forms.IntegerField()
    upper_test_mark = forms.IntegerField()


    class Meta:
        model = Product
        # exclude = ("user", )
        fields = ['title', 'category', 'table', 'no_of_samples', 'low_test_mark', 'upper_test_mark',]


# your_app/forms.py

# from django import forms
# from .models import Exercise

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['product', 'item_No', 'x_val', 'y_val', 'z_val', 'o_val', 'p_val', 'q_val']

# your_app/forms.py

# from django import forms
# from .models import Category, Product

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'slug']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['created_by', 'created', 'updated']
