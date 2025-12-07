from vercel_python.serverless import serverless_wsgi
from django.core.wsgi import get_wsgi_application

app = get_wsgi_application()
handler = serverless_wsgi(app)
