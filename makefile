ENV=.env
PYTHONPATH := $(shell pwd)
STREAMLIT_APP := main.py

setup:
	pipenv install --dev

shell:
	@echo "Activando entorno y exportando PYTHONPATH..."
	PYTHONPATH=$(PYTHONPATH) pipenv shell

run:
	PYTHONPATH=$(PYTHONPATH) pipenv run streamlit run $(STREAMLIT_APP)

lock:
	pipenv lock

clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	rm -rf .mypy_cache .pytest_cache

help:
	@echo "Comandos disponibles:"
	@echo "  setup        - Instala dependencias"
	@echo "  shell        - Activa entorno con PYTHONPATH"
	@echo "  run          - Ejecuta la app Streamlit"
	@echo "  lint         - Formatea código con black"
	@echo "  lock         - Genera Pipfile.lock"
	@echo "  clean        - Elimina archivos temporales"
