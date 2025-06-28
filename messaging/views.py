from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Mensaje
from .forms import MensajeForm

@login_required
def bandeja_view(request):
    mensajes = Mensaje.objects.filter(receptor=request.user).order_by('-fecha')
    return render(request, 'messaging/bandeja.html', {'mensajes': mensajes})

@login_required
def detalle_mensaje_view(request, pk):
    mensaje = get_object_or_404(Mensaje, pk=pk, receptor=request.user)
    if not mensaje.leido:
        mensaje.leido = True
        mensaje.save()
    return render(request, 'messaging/detalle.html', {'mensaje': mensaje})

@login_required
def enviar_mensaje_view(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.emisor = request.user
            mensaje.save()
            return redirect('bandeja')
    else:
        form = MensajeForm()
    return render(request, 'messaging/enviar.html', {'form': form})