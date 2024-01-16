from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="Authentication system API Documentation",
        default_version='v1',
        description="This is an `API documentation` for "
                    "the [Authentication system]( http://127.0.0.1:8000/) "
                    "Django Rest Framework project.\n"
                    "The `swagger-ui` view can be found [here](/swagger). The `ReDoc` view can be found "
                    "[here](/redoc).\n The `swagger YAML` document can be found [here](/swagger.yaml).",

        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="admin@gmail.com"),
        license=openapi.License(name="User_authentication License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=[],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', include('users.urls')),
]