import streamlit as st
from collections import namedtuple

Sentence = namedtuple("Sentence", ["title", "value"])


class Barthel:
    def __init__(self):
        self.name = "Escala de Barthel"
        self.blocks = [
            {
                "title": "Passagem cadeira-cama",
                "sentences": [
                    Sentence("Dependente", 0),
                    Sentence(
                        "Grande ajuda - É capaz de sentar-se, mas necessira de ajuda total para a mudança para a cama",
                        5,
                    ),
                    Sentence(
                        "Ajuda mínima - Necessita de pequena ajuda ou supervisão", 10
                    ),
                    Sentence(
                        "Independente - Não necessite de ajuda. Se utilixa cadeira de rosas, faz tudo isso sozinho",
                        15,
                    ),
                ],
                "value": None,
            },
            {
                "title": "Deambulação",
                "sentences": [
                    Sentence("Dependente", 0),
                    Sentence(
                        "Independente em cadeira de rodas- Movimenta-se na sua cadeira de rodas por pelo menos 50 metros",
                        5,
                    ),
                    Sentence(
                        "Ajuda - Pode caminhas pelo menos 50 metros, mas necessita de ajuda ou supervisão",
                        10,
                    ),
                    Sentence(
                        "Independente - Pode caminhar pelo menos 50 metros, mesmo com bengalas, muletas, prótese ou andador",
                        15,
                    ),
                ],
                "value": None,
            },
            {
                "title": "Escadas",
                "sentences": [
                    Sentence("Dependente", 0),
                    Sentence("Ajuda - Necessita de ajuda física ou supervisão", 5),
                    Sentence(
                        "Independente - É capaz de subir ou descer escadas sem ajuda ou supervisão, mesmo com muletas ou bengalas",
                        10,
                    ),
                ],
                "value": None,
            },
        ]
        self.min = 0
        self.max = sum(
            [block["sentences"][-1].value for block in self.blocks]
        )  # last value is the largest

    def render(self):
        with st.expander("Escale de Barthel"):
            for block in self.blocks:
                pos = st.selectbox(
                    block["title"],
                    list(range(len(block["sentences"]))),
                    format_func=lambda x: block["sentences"][x].title,
                )
                block["value"] = block["sentences"][pos].value
        self.value = sum([block["value"] for block in self.blocks])
