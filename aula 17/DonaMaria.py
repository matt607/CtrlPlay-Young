import ProjetoChatBot as pc 
nome_maquina = 'Maria'
pc.saudacoes(nome_maquina)
while True:
    texto = pc.receberTexto()
    resposta = pc.buscaResposta(nome_maquina, texto)
    if pc.exibeResposta(resposta, nome_maquina) == 'fim':
        break