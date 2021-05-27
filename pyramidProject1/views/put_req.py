from ..models.mymodel import MyModel


def put(request):
    try:
        obj = request.dbsession.query(MyModel).filter(MyModel.id == request.matchdict['id'])
        obj.update(request.json)
        return {'notes': [
            {'id': note.id, 'title': note.title, 'description': note.description,
             'create_at': note.create_at, 'create_by': note.create_by, 'priority': note.priority}

            for note in request.dbsession.query(MyModel)

        ]
        }
    except:
        return {'result': 'No object found'}
