from django.shortcuts import render
from django.core.mail import EmailMessage, mail_admins, BadHeaderError
from templated_mail.mail import BaseEmailMessage
import requests
import logging
from playground.tasks import notify_customers
from django.core.cache import cache
from django.utils.decorators import method_decorator
from django.views.decorators.cache  import cache_page
from rest_framework.views import APIView

logger = logging.getLogger(__name__)


class HelloView(APIView):
    #@method_decorator(cache_page(5*60))
    def get(self, request):
        try:
            logger.info('calling  httpbin')
            response = requests.get('https://httpbin.org/delay/2')
            logger.info('Received the response')
            data = response.json()
            #notify_customers.delay('Hello')
        except requests.ConnectionError:
            logger.critical('httpbin is offline')
        return render(request, 'hello.html', {'name': data})




    
  