# reSHP

Ferramenta desenvolvida para auxiliar a extração de valores de retângulo envolvente de arquivos do tipo Shapefile. 
Foi desenvolvida juntamente com o sistema edpMGBs (http://ide.dpi.ufv.br/edpmgbs/ ou https://github.com/MoisesHenr/edpMGBs) durante o período de vigência de bolsa de Iniciação Científica financiado pela CNPq.

Para testar o código recomenda-se:

. Anaconda Python (https://www.anaconda.com/distribution/);
. Com Anaconda Python instalado: instalar Pyshp (https://anaconda.org/conda-forge/pyshp);

Caso queira fazer um executável do código:

. Instalar Pyinstaller (https://anaconda.org/conda-forge/pyinstaller);

Com Pyinstaller instalado, pode-se acessar a pasta do reSHP e atráves do conda terminal usar o comando: pyinstaller reSHP.py --onefile --noconsole 
O executável desejado estará no diretório dist/, recém gerado.

Para mais informações sobre Pyinstaller: https://pyinstaller.readthedocs.io/en/stable/usage.html.

Obs: ferramenta reSHP desenvolvida e testada em Windows.
