from processamento import Processamento

from pprint import pprint

def main():
    deletar_uuids = []
    processamento = Processamento()

    dados_duplicados = processamento.documentos_duplicados()

    for dado in dados_duplicados:
        uuids = processamento.buscar_uuid(dado)


        
if __name__ == '__main__':
    main()