from django.shortcuts import render
from .models import *
from .forms import *
import os
import io
from reportlab.pdfgen import canvas
from django.http import FileResponse, HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.conf import settings
from django.db.models.signals import pre_delete
from django.dispatch import receiver
import datetime



## Действие при удалении билета !!!!!!!!!!!!!!!!
@receiver(pre_delete, sender=Tickets)
def my_function_post_save(sender,instance,**kwargs):
    print("Deleter !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print(instance.normal_ticket)
    print(sender.normal_ticket)



def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    # use short variable names
    sUrl = settings.STATIC_URL      # Typically /static/
    sRoot = settings.STATIC_ROOT    # Typically /home/userX/project_static/
    mUrl = settings.MEDIA_URL       # Typically /static/media/
    mRoot = settings.MEDIA_ROOT     # Typically /home/userX/project_static/media/

    # convert URIs to absolute system paths
    if uri.startswith(mUrl):
        path = os.path.join(mRoot, uri.replace(mUrl, ""))
    elif uri.startswith(sUrl):
        path = os.path.join(sRoot, uri.replace(sUrl, ""))
    else:
        return uri  # handle absolute uri (ie: http://some.tld/foo.png)

    # make sure that file exists
    if not os.path.isfile(path):
            raise Exception(
                'media URI must start with %s or %s' % (sUrl, mUrl)
            )
    return path


def render_pdf_view(request):
    template_path = 'control_panel.html'
    zz = Excursion.objects.all()
    pp=User.objects.filter(username=request.user)
    xx = Tickets.objects.get(pk=1).date
    context = {'zz': zz,'pp': pp,'xx': xx}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisaStatus = pisa.CreatePDF(html.encode("UTF-8"), dest=response, encoding='utf-8', link_callback=link_callback)
    # if error then show some funy view
    if pisaStatus.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def control_panel(request):
    if request.POST:
        print(request.POST)
        now = datetime.datetime.now()
        gg = Tickets.objects.all().filter(date__range=["2011-01-01", "2020-01-31"])
        print(gg)
        f = Tick(request.POST)
        f.save()
        form = Tick()
        return render(request, "control_panel.html", {"form": form})
    else:
        zz = Excursion.objects.all()
        pp = User.objects.all()
        xx = Tickets.objects.all()




        form = Tick()

    return render(request, "control_panel.html", {"form": form,"zz": zz,'pp': pp,'xx': xx})


def delet(request):
    if request.POST:
        pass
        # form = Fiz2_2_7(request.POST)
        # if form.is_valid():
        # pass
        # cd = form.cleaned_data
        # a = cd['a']
        # q = cd['q']
        # a *= 10 ** -2
        # q *= 10 ** -6
        # cont = 4 * q * a * 10 ** 9
        # moss = Money.objects.get(moneyname=request.user)
        # moss.moneyvalue -= fiz_zad
        # moss.save()
        # zzzzzzz = Money.objects.filter(moneyname=request.user)
        # for fffffff in zzzzzzz:
        #    jj = fffffff.moneyvalue
        # return render(request, "subj/fiz2_2_7.html", {"form": form, "cont": cont, "jj": jj, "fiz_zad": fiz_zad})
    else:
        pp = Tickets.objects.filter(pk=5).delete()
        print("asdd")
    return render(request, "control_panel.html", {})


def ticket_gen(request):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(100, 100, "Привет медвед.")
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')







