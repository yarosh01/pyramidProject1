from pyramid.view import view_config
from pyramid.response import Response
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import create_engine

from .. import models
from sqlalchemy import select
from ..models.mymodel import conn

@view_config(route_name='home', renderer='pyramidProject1:templates/mytemplate.jinja2')
def my_view(request):
    engine = create_engine('postgresql://dima:secret@localhost:5432/test_db')
    print(engine)
    conn = engine.connect()
    try:
        query = request.dbsession.query(models.MyModel)
        one = query.filter(models.MyModel.name == 'one').one()
        select_model = select(models.MyModel)
        print(select_model)
        result = conn.execute(select_model)
        for re in result:
            print(re)
    except SQLAlchemyError:
        return Response(db_err_msg, content_type='text/plain', status=500)
    return {'one': result, 'project': 'pyramidProject1'}

def get(request):

    try:
        return request.dbsession.query(models.MyModel).get(
            int(request.matchdict['id'])).to_json()
    except:
        return {}

db_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to initialize your database tables with `alembic`.
    Check your README.txt for descriptions and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""
