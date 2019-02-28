## mysite/views.py


from django.shortcuts import render
from mysite.models import UploadForm,Upload
from django.urls import reverse


from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from mysite.forms import ContactForm
from django.core.mail import EmailMessage, send_mail, BadHeaderError
from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.http import FileResponse, Http404


from django.views.generic import View







#from endless_pagination.decorators import page_template
#import re
#from django.contrib.messages import constants as messages



# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

# Add this view
# Instead of about.html I used index.html to direct the web page of work to index
class AboutPageView(TemplateView):
    template_name = "index.html"

# Add this view
class HomePageViewReal(TemplateView):
    template_name = "home.html"

# Add this view
class SuccessPageView(TemplateView):
    template_name = "success.html"


# Add this view
# Instead of work.html I used index.html to direct the web page of work to index
class WorkPageView(TemplateView):
    template_name = "index.html"


# Add this view
class ContactPageViewReal(TemplateView):
    template_name = "contact.html"

# Add this view
class AutomationTestingPageView(TemplateView):
    template_name = "automationtesting.html"

# Add this view
class NaturalLanguagePageView(TemplateView):
    template_name = "naturallanguage.html"

# Add this view
class TradingStockPageView(TemplateView):
    template_name = "tradingstock.html"

# Add this view
class MarkovProcessPageView(TemplateView):
    template_name = "markovprocess.html"


# Add this view
class ImpressumPageView(TemplateView):
    template_name = "impressum.html"




# Add this view
class SubmitMessagePageView():
    template_name = "ajax.php"



# Add this view
#template_name = "contact.html"
class ContactPageView():
    #template_name = "contact.html"
    def emailView(request):
        if request.method == 'GET':
            form = ContactForm()
        else:
            form = ContactForm(request.POST)
            if form.is_valid():
                #Telephone = form.cleaned_data['telephone']
                Email = form.cleaned_data['Email']
                #FirstName = form.cleaned_data['firstname']
                #LastName = form.cleaned_data['lastname']
                Message = form.cleaned_data['Message']
                Subject = form.cleaned_data['Subject']
                try:
                    send_mail(Email,Message,Subject, ['admin@example.com'])
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                return redirect('home')
        return render(request, "contact.html", {'form': form})


def SuccessView(request):
    return HttpResponse('Success! Thank you for your message.')


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})



# our view
def contact(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['ericnana@mail.com'],
                headers = {'Reply-To': contact_email }
            )

            #isValidEmail(contact_email) 


            if contact_name and contact_email and form_content:
               try:
                  email.send()
                  messages.success(request, 'Thank you! Your message has been successfully sent.')
                  return HttpResponseRedirect('/contact')
               except BadHeaderError:
                   messages.error(request, 'Sorry! Your message has not been sent.')
                   HttpResponse('Invalid e-mail header found.')
                   return HttpResponseRedirect('/contact')
            else:
               HttpResponse('Sorry your message has not been sent. Please make sure all fields are entered and valid')
               return HttpResponseRedirect('/contact')


            #email.send()
            #send_mail(subject,message,email_from,recipient_list)
            #messages.success(request, 'Successful! Your mail has been sent!')
            #return redirect('contact')
            
    #else:
       

    return render(request, 'contact.html', {'form': form_class,})



#messages.success(request, 'Mail succesfully sent.')
#messages.warning(request, 'Impossible to send mail.')
#messages.info(request, 'Through this you will be able to send mail.')
#messages.error(request, 'An error occured.')


'''
MESSAGE_TAGS = {
    messages.INFO: '',
    20: 'info',

    messages.SUCCESS: '',
    25: 'success',

    messages.WARNING: '',
    30: 'warning',

    messages.ERROR: '',
    40: 'error',

}
'''

'''
def isValidEmail(email):
  if len(email) > 7:
    if re.match("^.+@([?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email) != None:
     return True
  return False
'''
'''
def send_email(request):
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('from_email', '')
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['admin@example.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/contact/thanks/')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')
'''

'''
def pdf_view(request):
    try:
        return FileResponse(open('enter the path', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()
'''


'''
@page_template('templates/index.html')  # just add this decorator
def entry_index(
        request, template='templates/index.html', extra_context=None):
    context = {
        'entries': Entry.objects.all(),
    }
    if extra_context is not None:
        context.update(extra_context)
    return render_to_response(
        template, context, context_instance=RequestContext(request))

'''



# gallery/views.py

'''
from braces.views import (
    AjaxResponseMixin,
    JSONResponseMixin,
    LoginRequiredMixin,
    SuperuserRequiredMixin,
)

from calazanblog.gallery.models import Album, Photo


NaturalLanguagePageView(LoginRequiredMixin,
                    SuperuserRequiredMixin,
                    JSONResponseMixin,
                    AjaxResponseMixin,
                    View)
"""
    View for uploading photos via AJAX.
"""
def post_ajax(self, request, *args, **kwargs):
    try:
        album = Album.objects.get(pk=kwargs.get('pk'))
    except Album.DoesNotExist:
            error_dict = {'message': 'Album not found.'}
            return self.render_json_response(error_dict, status=404)

    uploaded_file = request.FILES['file']
    Photo.objects.create(album=album, file=uploaded_file)

    response_dict = {
            'message': 'File uploaded successfully!',
        }

    return self.render_json_response(response_dict, status=200)
'''

'''
def naturallanguage(request):
    if request.method=="POST":
        img = UploadForm(request.POST, request.FILES)       
        if img.is_valid():
            img.save()  
            return HttpResponseRedirect(reverse('imageupload'))
    else:
        img=UploadForm()
    images=Upload.objects.all().order_by('-upload_date')
    return render(request,'naturallanguage.html',{'form':img,'images':images})
'''
'''
def home(request):
    return render(request, 'naturallanguage.html', {'what':'Django File Upload'})
 
def naturallanguage(request):
    if request.method == 'POST':
        handle_uploaded_file(request.FILES['file'], str(request.FILES['file']))
        return HttpResponse("Successful")
 
    return HttpResponse("Failed")
 
def handle_uploaded_file(file, filename):
    if not os.path.exists('naturallanguage/'):
        os.mkdir('naturallanguage/')
 
    with open('naturallanguage/' + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
'''



'''
@baseline_model(self)
def func(request):
    return render("naturallanguage.html")
'''
