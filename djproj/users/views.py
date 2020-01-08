
# ^ for flash messages to show success or some kind of one time sign
from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def register(request):
    """
    Django’s login form is returned using the POST method, in which the browser bundles up the
    form data, encodes it for transmission, sends it to the server, and then receives back its response.
    :param request:
    :return:
    """
    if request.method == "POST":
        form = UserRegisterForm(request.POST)  # if post request is received, then a form will be made with that data.
        if form.is_valid():
            form.save()  # ensures that we save the user info to our db.
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}. Please login to continue')  # fstring is basically str.format()
            return redirect('login')
    else:
        form = UserRegisterForm()  # Create an instance of the user registration form. blank form.

    return render(request, 'users/register.html', {'form': form})


@login_required
# python decorators add functionalities to existing function,
# in this instance making sure that user is logged in to access this function
def profile(request):
    """
    To limit and separate functions for authenticated and non-authenticated users.
    :param request:
    :return:
    """

    return render(request, 'users/profile.html')