from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class CustomAuthToken(ObtainAuthToken):
    def post(self,request,*args,**kwargs):
        response = {
            "name":"viral"
        }
        serializer = self.serializer_class(data=request.data,context=response)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user' ]
        token,created = Token.objects.get_or_create(user=user)
        token_response = {
            'token':token.key,
            'password':user.password,
            'user_id':user.id,
            'email':user.email
        }
        return Response(token_response)