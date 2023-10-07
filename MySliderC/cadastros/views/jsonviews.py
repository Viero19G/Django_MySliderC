# Em views.py
from django.http import JsonResponse
from carrosselApp.models import *

def conteudo_grade_json(request, grade_id):
    try:
        grade = Grade.objects.get(id=grade_id)

        # Consulta para obter os conteúdos de tipo 'imagem' desta grade e seus IDs originais
        conteudo_imagem = Conteudo.objects.filter(grade=grade, tipo='imagem').order_by('id')
        imagem_data = [{'id': conteudo.id,'tempo':conteudo.imagem.tempo, 'url': conteudo.imagem.image.url} for conteudo in conteudo_imagem]

        # Consulta para obter os conteúdos de tipo 'video' desta grade e seus IDs originais
        conteudo_video = Conteudo.objects.filter(grade=grade, tipo='video').order_by('id')
        video_data = [{'id': conteudo.id, 'url': conteudo.video.video.url} for conteudo in conteudo_video]

        # Crie um dicionário com as informações da grade e as listas de URLs de imagem e vídeo
        grade_info = {
            'grade_id': grade.id,
            'grade_nome': grade.title,  # Substitua 'title' pelo campo correto
            'imagem_urls': imagem_data,
            'video_urls': video_data
        }

        return JsonResponse(grade_info)
    except Grade.DoesNotExist:
        return JsonResponse({'error': 'Grade não encontrada'}, status=404)
