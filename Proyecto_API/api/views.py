from django.shortcuts import render
from .models import Usuario
from django.views import View
from django.utils.decorators import method_decorator
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
class UsuarioView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request, id=0):
        if (id > 0):
            usuarios = list(Usuario.objects.filter(id=id).values())
            if len(usuarios) > 0:
                usuario = usuarios[0]
                datos = {'message': "Success", 'usuario': usuario}
            else:
                datos = {'message': "Usuario no encontrado..."}
            return JsonResponse(datos)
        else:
            usuarios = list(Usuario.objects.values())
            if len(usuarios) > 0:
                #usuario = usuarios[0]
                datos = {'message': "Success", 'usuario': usuarios}
            else:
                datos = {'message': "Usuarios no encontrados..."}
            return JsonResponse(datos)
    
    def post(self,request):
        jd = json.loads(request.body)
        Usuario.objects.create(nombre=jd['nombre'], cedula=jd['cedula'], telefono=jd['telefono'], correo=jd['correo'], clave=jd['clave'], numCuenta=jd['numCuenta'],  saldo=jd['saldo'] )
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self,request, id):
        jd = json.loads(request.body)
        usuarios = list(Usuario.objects.filter(id=id).values())
        if len(usuarios) > 0:
            usuario = Usuario.objects.get(id=id)
            usuario.nombre = jd['nombre']
            usuario.cedula = jd['cedula']
            usuario.telefono = jd['telefono']
            usuario.correo = jd['correo']
            usuario.clave = jd['clave']
            usuario.numCuenta = jd['numCuenta']
            usuario.saldo = jd['saldo']
            usuario.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Usuario no encontrado..."}
        return JsonResponse(datos)
    
    def delete(self,request, id):
        usuarios = list(Usuario.objects.filter(id=id).values())
        if len(usuarios) > 0:
            Usuario.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Usuario no encontrado..."}
        return JsonResponse(datos)
