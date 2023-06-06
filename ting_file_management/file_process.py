import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    position = len(instance)

    for index in range(position):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return None

    lines = txt_importer(path_file)

    if len(lines) > 0:
        file_data = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(lines),
            "linhas_do_arquivo": lines
        }
        instance.enqueue(file_data)

        print(file_data, file=sys.stdout)
    else:
        print(f"Arquivo {path_file} está vazio. Ignorando.", file=sys.stdout)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
