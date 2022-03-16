import streamlit as st


class LawtonScale:
    def __init__(self):
        self.blocks = [
            {
                "title": "Telefone",
                "sentences": [
                    "Incapaz de usar o telefone",
                    "Assistência para ligações ou telefone especial",
                    "Recebe e faz ligações sem assistência",
                ],
                "response": None,
            },
            {
                "title": "Viagens",
                "sentences": [
                    "Incapaz de viajar",
                    "Viaja Exclusivamente acompanhado",
                    "Viaja sozinho",
                ],
                "response": None,
            },
            {
                "title": "Compras",
                "sentences": [
                    "Incapaz de fazer compras",
                    "Faz compras acompanhado",
                    "Faz compras, se fornecido o transporte",
                ],
                "response": None,
            },
            {
                "title": "Preparo de refeições",
                "sentences": [
                    "Incapaz",
                    "Prepara só pequenas refeições",
                    "Planeja e cozinha refeições completas",
                ],
                "response": None,
            },
            {
                "title": "Trabalho doméstico",
                "sentences": [
                    "Incapaz",
                    "Tarefas leves, com ajuda nas pesadas",
                    "Tarefas pesadas",
                ],
                "response": None,
            },
            {
                "title": "Medicações",
                "sentences": [
                    "Incapaz de tomar sozinho",
                    "Necessita de lembretes de assistência",
                    "Toma remédios sem assistência",
                ],
                "response": None,
            },
            {
                "title": "Dinheiro",
                "sentences": [
                    "Incapaz",
                    "Assistência para cheque e contas",
                    "Preenche cheques e paga contas",
                ],
                "response": None,
            },
        ]
        self.min = len(self.blocks)
        self.max = 3 * len(self.blocks)

    @staticmethod
    def _translate(sentence):
        return {
            "Recebe e faz ligações sem assistência": 3,
            "Assistência para ligações ou telefone especial": 2,
            "Incapaz de usar o telefone": 1,
            "Viaja sozinho": 3,
            "Viaja Exclusivamente acompanhado": 2,
            "Incapaz de viajar": 1,
            "Incapaz de fazer compras": 1,
            "Faz compras acompanhado": 2,
            "Faz compras, se fornecido o transporte": 3,
            "Incapaz": 1,
            "Prepara só pequenas refeições": 2,
            "Planeja e cozinha refeições completas": 3,
            "Incapaz": 1,
            "Tarefas leves, com ajuda nas pesadas": 2,
            "Tarefas pesadas": 3,
            "Incapaz de tomar sozinho": 1,
            "Necessita de lembretes de assistência": 2,
            "Toma remédios sem assistência": 3,
            "Incapaz de tomar sozinho": 1,
            "Necessita de lembretes de assistência": 2,
            "Toma remédios sem assistência": 3,
        }.get(sentence, 0)

    def render(self):
        with st.expander("Escala de Lawton"):
            for block in self.blocks:
                block["response"] = st.selectbox(block["title"], block["sentences"])
        self.value = sum([self._translate(block["response"]) for block in self.blocks])
