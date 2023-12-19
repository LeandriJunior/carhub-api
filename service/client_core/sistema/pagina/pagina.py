from django.db.models import F

from client_core.pagina import models


class Pagina:
    @staticmethod
    def get_pagina(pagina=None):
        pagina = models.Pagina.objects.filter(status=True, nome=pagina).values(
            background_color=F('configuracao__background_color'),
            logo=F('configuracao__logo'),
            config=F('configuracao__configuracao')
        ).first()

        return {
            'status': True if pagina else False,
            'descricao': '' if pagina else 'Nenhuma pagina encotrada',
            'dados': pagina
        }