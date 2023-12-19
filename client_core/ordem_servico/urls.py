from client_core.ordem_servico import views
urlpatterns = [
    re_path('ordem-servico', views.OrdemServicoView.as_view())
]
