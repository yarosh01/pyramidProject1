from ..models.mymodel import MyModel


def collection_post(request):
    note = request.json
    request.dbsession.add(MyModel.from_json(note))
