#!/usr/bin/env python3

import subprocess as sp; import sys;

def nto2png(path_dir:str) -> None:
    print("\nCRIANDO ARQUIVO 'LISTA_NTO' E DIRETÓRIO 'TEXTURES'...\n")
    sp.run(f"find {path_dir} -name *.nto > ./lista_nto.txt; mkdir Textures",shell=True);
    print("\nCONVERTENDO ARQUIVOS '.nto' PARA '.png'...\n")
    with open("./lista_nto.txt","r") as arquivo:
        for linha in arquivo.readlines():
            linha = str(linha).removesuffix("\n");
            sp.run(f"wine nto2img.exe -i {linha} -f p -o ./Textures/$(basename {linha})", shell=True);
    print("\nCONVERSÃO FINALIZADA.\n")

def nmo2lwo(path_dir:str) -> None:
    print("\nCRIANDO ARQUIVO 'LISTA_NMO' E DIRETÓRIO 'Models'...\n")
    sp.run(f"find {path_dir} -name *.nmo > ./lista_nmo.txt; mkdir Models",shell=True)
    print("\nCONVERTENDO ARQUIVOS '.nmo' PARA '.lwo'...\n")
    with open("./lista_nmo.txt","r") as arquivo:
        for linha in arquivo.readlines():
            print(linha)
            linha = str(linha).removesuffix("\n");
            sp.run(f"wine nmo2lwo.exe -i {linha} -o ./Models/$(basename {linha})", shell=True);
    print("\nCONVERSÃO FINALIZADA.\n")


if (len(sys.argv) ==  1):
    print("""       
    Ajuda:

	Conversor de textura '.nto' para .png e de modelo 3D '.nmo' para .lwo.

    ----   ----   ----   ----   ----   ----   ----   ----   ----   ----   ----   ----   ----   ----   ----   ----
    ----   ----   ----   ----   ----   ----   ----   ----   ----   ----   ----   ----   ----   ----   ----   ----
          
    Uso: ./SotC_ntmo_converter.py [path_dir/NICO.DAT_DIR[/]] [1 | 2] 
          
    Parâmetros:

	--- O 1º parâmetro deve ser o path do diretório 'NICO.DAT_DIR'.

	--- O 2º parâmetro deve ser umas das opções do seguinte conjunto {1,2}:

		 1 -> Converter todas as texturas '.nto' para '.png'.
		 2 -> Converter todos os modelos '.nmo' para '.lwo'.
        """)

elif (len(sys.argv) == 3):
    if ((sys.argv[1][len(sys.argv[1]) - 12:len(sys.argv[1])] == "NICO.DAT_DIR" or sys.argv[1][len(sys.argv[1]) - 13:len(sys.argv[1])]  == "NICO.DAT_DIR/") and sys.argv[2] in "12"):
        if sys.argv[2] == "1":
            nto2png(sys.argv[1])
        else:
            nmo2lwo(sys.argv[1])
    else:
        print("Insira um nome válido do diretório NICO e/ou insira uma opção de conversão válida, conforme detalhado em ajuda.")
else:
    print("Insira zero argumento para obter ajuda")
