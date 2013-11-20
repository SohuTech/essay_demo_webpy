#coding:utf-8

import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))

from fabric.state import env

from essay.tasks import build
from essay.tasks import deploy
#from essay.tasks import nginx
#from essay.tasks import supervisor

env.GIT_SERVER = 'https://github.com/'  # ssh地址只需要填：github.com
env.PROJECT = 'essay_demo_webpy'
env.DEPLOY_PATH = '~/buildspace'
env.PROJECT_OWNER = 'EssayTech'
env.DEFAULT_BRANCH = 'master'
env.PYPI_INDEX = 'http://pypi.python.org/simple/'


######
# deploy settings:
env.PROCESS_COUNT = 2  #部署时启动的进程数目
env.roledefs = {
    'build': ['vagrant@127.0.0.1:2202'],  # 打包服务器配置
    'dev': [''],
}

env.VIRTUALENV_PREFIX = '/home/django/essay_demo_webpy'
env.SUPERVISOR_CONF_TEMPLATE = os.path.join(PROJECT_ROOT, 'conf', 'supervisord.conf')
