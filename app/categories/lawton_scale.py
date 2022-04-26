import streamlit as st
from collections import namedtuple

Sentence = namedtuple("Sentence", ["title", "value"])


class LawtonScale:
    def __init__(self):
        self.name = "Lawton"
        self.blocks = [
            {
                "title": "Telefone",
                "sentences": [
                    Sentence("Incapaz de usar o telefone", 1),
                    Sentence("Assistência para ligações ou telefone especial", 2),
                    Sentence("Recebe e faz ligações sem assistência", 3),
                ],
                "value": None,
            },
            {
                "title": "Viagens",
                "sentences": [
                    Sentence("Incapaz de viajar", 1),
                    Sentence("Viaja Exclusivamente acompanhado", 2),
                    Sentence("Viaja sozinho", 3),
                ],
                "value": None,
            },
            {
                "title": "Compras",
                "sentences": [
                    Sentence("Incapaz de fazer compras", 1),
                    Sentence("Faz compras acompanhado", 2),
                    Sentence("Faz compras, se fornecido o transporte", 3),
                ],
                "value": None,
            },
            {
                "title": "Preparo de refeições",
                "sentences": [
                    Sentence("Incapaz", 1),
                    Sentence("Prepara só pequenas refeições", 2),
                    Sentence("Planeja e cozinha refeições completas", 3),
                ],
                "value": None,
            },
            {
                "title": "Trabalho doméstico",
                "sentences": [
                    Sentence("Incapaz", 1),
                    Sentence("Tarefas leves, com ajuda nas pesadas", 2),
                    Sentence("Tarefas pesadas", 3),
                ],
                "value": None,
            },
            {
                "title": "Medicações",
                "sentences": [
                    Sentence("Incapaz de tomar sozinho", 1),
                    Sentence("Necessita de lembretes de assistência", 2),
                    Sentence("Toma remédios sem assistência", 3),
                ],
                "value": None,
            },
            {
                "title": "Dinheiro",
                "sentences": [
                    Sentence("Incapaz", 1),
                    Sentence("Assistência para cheque e contas", 2),
                    Sentence("Preenche cheques e paga contas", 3),
                ],
                "value": None,
            },
        ]
        self.min = len(self.blocks)
        self.max = 3 * len(self.blocks)

    def render(self):
        with st.expander("Escala de Lawton"):
            for block in self.blocks:
                pos = st.selectbox(
                    block["title"],
                    list(range(len(block["sentences"]))),
                    format_func=lambda x: block["sentences"][x].title,
                )
                block["value"] = block["sentences"][pos].value
        self.value = sum([block["value"] for block in self.blocks])
