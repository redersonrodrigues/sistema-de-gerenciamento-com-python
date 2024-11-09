import os
import xml.etree.ElementTree as Et
from datetime import date


class Read_xml:
    def __init__(self, directory) -> None:
        self.directory = directory

    # ler todos arquivos xll da pasta
    def all_files(self):
        return [
            os.path.join(self.directory, arq)
            for arq in os.listdir(self.directory)
            if arq.lower().endswith(".xml")
        ]

    def nfe_data(self, xml):
        root = Et.parse(xml).getroot()
        nsNfe = {"ns": "http://www.portalfiscal.inf.br/nfe"}

        # Dados da NFE (parseando)
        NFe = self.check_none(root.find("./ns:NFe/ns:infNfe/ns:ide/ns:nNF", nsNfe))  # 1
        serie = self.check_none(
            root.find("./ns:NFe/ns:infNfe/ns:ide/ns:serie", nsNfe)
        )  # 2
        data_emissao = self.check_none(
            root.find("./ns:NFe/ns:infNfe/ns:ide/ns:dhEmi", nsNfe)
        )  # 3
        data_emissao = f"{data_emissao[8:10]}/{data_emissao[5:7]}/{data_emissao[:4]}"  # formatando data com slice

        # Dados dos  Emitentes(parseando)
        chave = self.check_none(
            root.find("./ns:protNFe/ns:infProt/ns:chNFe", nsNfe)
        )  # 1
        cnpj_emitente = self.check_none(
            root.find("./ns:NFe/ns:infNfe/ns:emit/ns:CNPJ", nsNfe)
        )  # 2
        nome_emitente = self.check_none(
            root.find("./ns:NFe/ns:infNfe/ns:emit/ns:xNome", nsNfe)
        )  # 3

        cnpj_emitente = self.format_cnpj(
            cnpj_emitente
        )  # formatando cnpj com método criado para isto
        valorNfe = self.check_none(
            root.find("./ns:NFe/ns:infNFe/ns:total/ns:ICMSTot/ns:vNF", nsNfe)
        )
        data_importacao = date.today()
        data_importacao = data_importacao.strftime("%d/%m/%Y")
        data_saida = ""
        usuario = ""

        itemNota = 1
        notas = []

        for item in root.findall("./ns:NFe/ns:infNFe/ns:det", nsNfe):
            # Dados do item =====================================
            cod = self.check_none(item.find(".ns:prod/ns:cProd", nsNfe))
            qntd = self.check_none(item.find(".ns:prod/ns:qCom", nsNfe))
            descricao = self.check_none(item.find(".ns:prod/ns:xProd", nsNfe))
            unidade_medida = self.check_none(item.find(".ns:prod/ns:uCom", nsNfe))
            valorProd = self.check_none(item.find(".ns:prod/ns:vProd", nsNfe))

            dados = [
                NFe,
                serie,
                data_emissao,
                chave,
                cnpj_emitente,
                nome_emitente,
                valorNfe,
                itemNota,
                cod,
                qntd,
                descricao,
                unidade_medida,
                valorProd,
                data_importacao,
                usuario,
                data_saida,
            ]

            notas.append(dados)
            itemNota += 1
        return notas

    def check_none(self, var):
        if var == None:
            return ""
        else:
            try:
                return var.text.replace(".", ",")
            except:
                return var.text

    def format_cnpj(self, cnpj):
        try:

            cnpj = f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}"
            return cnpj

        except:
            return ""


if __name__ == "__main__":
    xml = Read_xml(
        "C:\\Users\\ratal\\OneDrive\\Estudo\\PyTax\\Interface - Pyside2\\Projeto_01_system\\xml"
    )
    all = xml.all_files()

    for i in all:
        result = xml.nfe_data(i)

    print(result)
