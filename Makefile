build:
	docker build -t streamlit-radar:latest .
.PHOYN: build

run:
	docker run --rm -it -p 8501:8501 streamlit-radar:latest
.PHONY: run

bash:
	docker run --rm -it -p 8501:8501 --entrypoint /bin/bash streamlit-radar:latest
.PHONY: bash
