#!/bin/bash

if [[ $# -eq 0 ]]; then

	echo -e "\nUso:
	./SotC_ntmo_converter.sh [path/NICO.DAT_DIR] [ 1 | 2 ]
	
Parâmetros:
	1º -> Caminho do diretório NICO.DAT
	2º -> Uma das opções do seguinte set {1,2}:
		1 -> Converte todas as texturas nto para png.
		2 -> Converte todos os modelos nmo para lwo.
"

elif [[ $# -eq 2 ]]; then
	if [[ ($1 -eq 1 || $1 -eq 2) && $(basename $2) == "NICO.DAT_DIR" ]]; then
		if [[ $1 -eq 1 ]]; then
			find $2 -name *.nto > lista_nto.txt; mkdir Texturas
			for line in $(cat lista_nto.txt); do
				wine nto2img.exe -i $line -f p -o ./Texturas/$(basename -s .nto $line)
				
			done
			clear
			echo -e "\nConversão Finalizada. Liste o diretório corrente para encontrar seus arquivos.\n"
		else 
			find $2 -name *.nmo > lista_nmo.txt; mkdir Modelos
			cat lista_nmo.txt
			for line in $(cat lista_nmo.txt); do
				wine nmo2lwo.exe -i $line  -o ./Modelos/$(basename -s .nmo $line)
			done
			clear
			echo -e "\nConversão Finalizada. Liste o diretório corrente para encontrar seus arquivos.\n"
		fi

	else echo "Insira o caminho válido para o diretório NICO e/ou digite uma opção válida."
	fi
else echo -e "\nErro! Verifique a descrição de usabilidade do programa.\n"
fi
