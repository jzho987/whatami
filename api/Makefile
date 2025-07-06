all: generate-golang generate-typescript generate-python

generate-golang:
	openapi-generator generate -i openapi.yaml -g go -o ./golang

generate-typescript:
	openapi-generator generate -i openapi.yaml -g typescript-axios -o ./typescript

generate-python:
	openapi-generator generate -i openapi.yaml -g python -o ./python
