def get_stamina_color(stamina):
    """
    Retorna a cor da barra de stamina com base no percentual de stamina.
    """
    if stamina > 50:
        return "#00BFFF"  # Azul claro (indica boa resistência)
    elif stamina > 20:
        return "#FFD700"  # Amarelo (indica avaliação neutra)
    else:
        return "#FF6347"  # Tomate (stamina baixa ou quase acabada)


def get_cor_vida(vida):
    """
    Retorna a cor da barra de vida com base no percentual de vida.
    """
    if vida > 50:
        return "#00FF00"  # Verde
    elif vida > 20:
        return "#FFFF00"  # Amarelo
    else:
        return "#FF0000"  # Vermelho
