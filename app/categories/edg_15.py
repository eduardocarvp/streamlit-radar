import streamlit as st
from collections import namedtuple

Sentence = namedtuple("Sentence", ["title", "value"])


class EDG:
    def __init__(self):
        self.name = "EDG-15"
        self.blocks = [
            {
                "title": "Você está basicamente satisfeito com sua vida?",
                "sentences": [
                    Sentence("Não", 1),
                    Sentence("Sim", 0),
                ],
                "value": None,
            },
            {
                "title": "Você deixou muito de seus interesses e atividades?",
                "sentences": [
                    Sentence("Não", 0),
                    Sentence("Sim", 1),
                ],
                "value": None,
            },
            {
                "title": "VocÊ sente que sua vida está vazia?",
                "sentences": [
                    Sentence("Não", 0),
                    Sentence("Sim", 1),
                ],
                "value": None,
            },
            {
                "title": "Você se aborrece com frequência?",
                "sentences": [
                    Sentence("Não", 0),
                    Sentence("Sim", 1),
                ],
                "value": None,
            },
            {
                "title": "Você se sente de bom humor a maior parte do tempo?",
                "sentences": [
                    Sentence("Não", 1),
                    Sentence("Sim", 0),
                ],
                "value": None,
            },
            {
                "title": "Você tem medo que algum mal vá lhe acontecer?",
                "sentences": [
                    Sentence("Não", 0),
                    Sentence("Sim", 1),
                ],
                "value": None,
            },
            {
                "title": "Você se sente feliz a maior parte do tempo?",
                "sentences": [
                    Sentence("Não", 1),
                    Sentence("Sim", 0),
                ],
                "value": None,
            },
            {
                "title": "Você sente que sua situação não tem saída?",
                "sentences": [
                    Sentence("Não", 1),
                    Sentence("Sim", 0),
                ],
                "value": None,
            },
            {
                "title": "Você prefere ficar em casa a sair e fazer coisas novas?",
                "sentences": [
                    Sentence("Não", 0),
                    Sentence("Sim", 1),
                ],
                "value": None,
            },
            {
                "title": "Você se sente com mais problemas de memória do que a maioria?",
                "sentences": [
                    Sentence("Não", 0),
                    Sentence("Sim", 1),
                ],
                "value": None,
            },
            {
                "title": "Você acha maravilhoso estar vivo?",
                "sentences": [
                    Sentence("Não", 1),
                    Sentence("Sim", 0),
                ],
                "value": None,
            },
            {
                "title": "Você se sente inútil nas atuais circunstâncias?",
                "sentences": [
                    Sentence("Não", 0),
                    Sentence("Sim", 1),
                ],
                "value": None,
            },
            {
                "title": "Você se sente cheio de energia?",
                "sentences": [
                    Sentence("Não", 1),
                    Sentence("Sim", 0),
                ],
                "value": None,
            },
            {
                "title": "Você acha que sua situação é sem esperanças?",
                "sentences": [
                    Sentence("Não", 0),
                    Sentence("Sim", 1),
                ],
                "value": None,
            },
            {
                "title": "Você sente que a maioria das pessoas está melhor que você?",
                "sentences": [
                    Sentence("Não", 0),
                    Sentence("Sim", 1),
                ],
                "value": None,
            },
        ]
        self.min = 0
        self.max = len(self.blocks)

    def render(self):
        with st.expander("Escala de depressão geriátrica versão curta (EDG-15)"):
            for block in self.blocks:
                pos = st.selectbox(
                    block["title"],
                    list(range(len(block["sentences"]))),
                    format_func=lambda x: block["sentences"][x].title,
                )
                block["value"] = block["sentences"][pos].value
        self.value = sum([block["value"] for block in self.blocks])
