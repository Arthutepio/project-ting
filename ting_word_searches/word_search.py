def exists_word(word, instance):
    results = []

    for file in range(len(instance)):
        file = instance.search(file)
        file_info = {
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": [],
            }

        for index, line in enumerate(file["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                file_info["ocorrencias"].append({"linha": index + 1})

        if file_info["ocorrencias"]:
            results.append(file_info)

    return results


def search_by_word(word, instance):
    result = exists_word(word, instance)

    for index in range(len(result)):
        for idx in range(len(instance)):
            file = instance.search(idx)

            if file["nome_do_arquivo"] == result[index]["arquivo"]:
                for i in range(len(result[index]["ocorrencias"])):
                    lines = file["linhas_do_arquivo"]
                    line_number = result[index]["ocorrencias"][i]["linha"]
                    content = lines[line_number - 1]
                    result[index]["ocorrencias"][i]["conteudo"] = content

    return result
