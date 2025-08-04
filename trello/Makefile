.PHONY: help list migrate


##--------------------------------------------------------
## Help
##--------------------------------------------------------
help: ## Mostrar esta ayuda
	@echo
	@echo "Usage: make [target]"
	@echo
	@echo "Targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) \
		| sort \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'
	@echo

##--------------------------------------------------------
## Project setup
##--------------------------------------------------------

requirements: ## Instalar dependencias
	pip install -r requirements.txt

web: ## Iniciar servidor web
	flet run ./src/main.py --web


##--------------------------------------------------------
## Utilidades genéricas
##--------------------------------------------------------

list: ## Listar todos los archivos del proyecto
	@find . -maxdepth 2 -print

