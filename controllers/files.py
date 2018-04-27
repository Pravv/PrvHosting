from ..models import utils, database


def files(filename):
    url, _ = utils.split_name_from_extension(filename)

    ok, match = database.find(url)
    if ok:
        return filesidad
