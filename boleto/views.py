from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rolepermissions.checkers import has_permission

from boleto.serializers import BoletoSerializer
from boleto.utils import make_boleto

class GenBoleto(APIView):
    def post(self, request):
        if has_permission(request.user, "can_generate_boleto"):
            serializer = BoletoSerializer(data=request.data)
            if serializer.is_valid():
                boleto = make_boleto(serializer.validated_data['modelo'], serializer.validated_data['campos'])
                return boleto
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'response': 'Nao possui permissoes para acessar esse recurso.'},
                        status=status.HTTP_401_UNAUTHORIZED)
