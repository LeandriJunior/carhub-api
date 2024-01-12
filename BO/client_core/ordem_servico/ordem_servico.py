import copy

import client_core.ordem_servico.models


class OrdemServico:
    def __init__(self):
        pass

    @staticmethod
    def template():
        dict = {
            'id': int,
            'cliente': str,
            'carro': str,
            'placa': str,
            'status': str,
            'is_aprovado': bool,
            'responsavel': str,
            'data_expedicao': str,
            'data_entrega': str,
            'hora_entrega': str,
        }

        return copy.deepcopy(dict)

    def get_ordem_servico(self):
        try:
            ordem_servico = client_core.ordem_servico.models.OrdemServico.objects.filter(
                status=True
            ).values(
                'id', 'cliente', 'carro', 'carro__placa', 'status_ordem', 'is_aprovado', 'responsavel', 'data_expedicao', 'data_entrega', 'hora_entrega'
            )

            for ordem in ordem_servico:
                template = OrdemServico.template()
                template['id'] = ordem.get('id')
                template['cliente'] = ordem.get('cliente_id__nome')
                template['carro'] = ordem.get('carro_id__nome')

            return True, '', ordens
        except:
            return False, '', []
