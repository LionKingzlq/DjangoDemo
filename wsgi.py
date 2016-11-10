import os
import sys
from imp import reload

# 将系统的编码设置为UTF8
reload(sys)
#sys.setdefaultencoding('utf8')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoDemo.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
