"""
    Faça um programa que peça o tamanho de um arquivo para download (em MB)
    e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo
    aproximado de download do arquivo usando este link (em minutos).

    Exercicio resolvido com base na resolução do repositório abaixo:
        https://github.com/selatotal/pythonBrasilExercicios/blob/master/01_EstruturaSequencial/18_taxa_transferencia.py
"""

tamanho_arquivo = float(input("Informe, em MB, o tamanho do arquivo:"))
velocidade_internet = int(input("Informe, em Mbps, a velocidade da internet:"))

conversao_tamanho_bits = tamanho_arquivo * 1024 * 1024 * 8
conversao_internet_mbps = velocidade_internet * 1024 * 1024
tempo_download_minutos = int((conversao_tamanho_bits / conversao_internet_mbps) / 60)

print(f"Tempo estimado para download do arquivo: {tempo_download_minutos} minutos")