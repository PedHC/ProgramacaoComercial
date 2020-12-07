from django.contrib.auth.mixins import LoginRequiredMixin

class AutenticacaoObrigatoria(LoginRequiredMixin):
    login_url = '/'