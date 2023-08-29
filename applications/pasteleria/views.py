from typing import Any, Dict
from django.shortcuts import render, redirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,
)
# CORREO
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages

# MODELS
from .models import Producto
#FORMS
from .forms import ContactForm

# Create your views here.

class InicioView(TemplateView):
    # VISTA PAGINA INICIO
    template_name = 'home/index.html'

class ListProductsClient(ListView):
    template_name = 'pasteleria/list_all.html'
    paginate_by = 4 # METODO PARA PAGINACION
    context_object_name = 'productos'
    model = Producto

class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'pasteleria/detail_product.html'
    context_object_name = 'producto'

    def get_context_data(self, **kwargs):
        context = super(ProductoDetailView, self).get_context_data(**kwargs)
        return context


class ContactoView(TemplateView):
    template_name = 'pasteleria/contacto.html'
    # Agregar formulario vacio en template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ContactForm()
        return context
    # Procesar los datos del formulario aquí
    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    # Lógica para manejar un formulario válido
    def form_valid(self, form):
        name = self.request.POST['name']
        email = self.request.POST['email']
        subject = self.request.POST['subject']
        content = self.request.POST['content']
        template = render_to_string('pasteleria/contact_form.html',{
            'name': name,
            'email': email,
            'content': content
        })
        email = EmailMessage(
            subject,
            template,
            settings.EMAIL_HOST_USER,
            ['pcbyto@gmail.com']
        )
        email.fail_silently = False
        email.send()
        messages.success(self.request, 'Se ha enviado tu correo.')
        print('correo enviado')
        return render(self.request, self.template_name, {'form': form})
    # Lógica para manejar un formulario inválido
    def form_invalid(self, form):
        print(form.errors)
        messages.error(self.request, 'Complete los campos y el captcha.')
        return render(self.request, self.template_name, {'form': form})
    