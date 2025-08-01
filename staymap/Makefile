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

migrate: ## Migrar base de datos
	PYTHONPATH=src python src/database/init_db.py


reset-db: ## Eliminar y volver a crear todas las tablas (pierdes datos)
	PYTHONPATH=src python src/database/init_db.py reset

seed-stops: ## Sembrar paradas de autobús por defecto
	PYTHONPATH=src python src/scripts/seed_stops.py

##--------------------------------------------------------
## Utilidades genéricas
##--------------------------------------------------------

list: ## Listar todos los archivos del proyecto
	@find . -maxdepth 2 -print

