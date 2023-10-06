from processamento import Processamento

from pprint import pprint

def main():
    processamento = Processamento()

    dados_duplicados = processamento.documentos_duplicados()

    for dado in dados_duplicados:
        uuids = processamento.buscar_uuid(dado)

        for uuid in uuids:
            pessoa = processamento.buscar_pessoa(uuid)


if __name__ == '__main__':
    main()