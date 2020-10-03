from invoke import task
import os

@task
def run(c, name, module):

    os.environ['LOAD_MODULE'] = module
    os.environ['NAME'] = name

    c.run('python3 __main__.py')
