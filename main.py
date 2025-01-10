import os
from flask import Flask, render_template_string, url_for, jsonify, request

from game.tools.colors import get_cor_vida, get_stamina_color
from game.player import NewPlayer
from game.world import NewWorld
from game.map import gerar_mapa, create_mini_map, salvar_mapa_html


app = Flask(__name__)

player = NewPlayer()
world = NewWorld()

# Gerar o mapa
largura_altura = 15  # Largura e Altura do mapa (colunas)
mapa_gerado = gerar_mapa(largura_altura)
salvar_mapa_html(mapa_gerado, "game/mapa.html")


def generate_full_html(player_status_html, midley_html, characters_present_html, map_html):
    """
    Gera o HTML contendo todas as 4 caixas no layout em grid.
    """
    css_style_url = url_for('static', filename='css/style.css')

    # Listar todos os arquivos da pasta 'static/js'
    scripts_folder = os.path.join('static', 'js')
    script_tags = ""
    if os.path.exists(scripts_folder):
        for script_name in os.listdir(scripts_folder):
            if script_name.endswith('.js'):  # Apenas arquivos .js
                script_url = url_for('static', filename=f'js/{script_name}')
                script_tags += f'<script src="{script_url}"></script>\n'

    return f"""
    <html>
    <head>
        <link rel="stylesheet" href="{css_style_url}">
        {script_tags}
    </head>
    <body>
        <div class="box" style="grid-column: 1; grid-row: span 2;">
            {player_status_html}
        </div>
        <div class="box" style="grid-column: 2; grid-row: span 2;">
            {midley_html}
            <button class="damage-button" onclick="takeDamage(5)">Take Damage (-5)</button>
            <button class="damage-button" onclick="takeStaminaDamage(5)">Take Stamina Damage (-5)</button>
        </div>
        <div class="box" style="grid-column: 3; grid-row: 1;">
            {characters_present_html}
        </div>
        <div class="box map-box" style="grid-column: 3; grid-row: 2;">
            {map_html}
        </div>
    </body>
    </html>
    """


def generate_html_player_status(content, player: NewPlayer, url_img: str):
    """
    Gera o conteúdo HTML para a caixa Player Status com a barra de vida e stamina.
    """
    formatted_content = "".join(
        f"<div class='player-text'>{item}</div>" for item in content
    )
    return f"""
    <h4>{player.first_name.title()} {player.last_name.title()}</h4>
    <div>
        <ul class="thm-list">
            <li>{player.title.title()}</li>
            <li>{world.dia}/{world.mes}/{world.ano} {world.hora}:{world.minuto}</li>
            <li>${player.money}</li>
        </ul>
    </div>
    <div class="player-box">
        <div class="player-image">
            <img src="{url_img}" alt="Imagem do jogador">
        </div>
        <div class="player-info">
            <h4>Status</h4>
            <div 
                class="health-bar" 
                style="width: 100%; height: 10px; background-color: #555; border: 1px solid #333; border-radius: 5px; margin-top: 10px; overflow: hidden;">
                <div 
                    id="player-life-bar"
                    title="Vida Atual: {player.health}%" 
                    style="width: {player.health}%; height: 100%; background-color: {get_cor_vida(player.health)};">
                </div>
            </div>
            <div 
                class="stamina-bar" 
                style="width: 100%; height: 10px; background-color: #555; border: 1px solid #333; border-radius: 5px; margin-top: 10px; overflow: hidden;">
                <div 
                    id="player-stamina-bar"
                    title="Stamina Atual: {player.stamina}%" 
                    style="width: {player.stamina}%; height: 100%; background-color: {get_stamina_color(player.stamina)};">
                </div>
            </div>
        </div>
        <div class="player-info">
            <h4>Effects</h4>
            <div>foo bar</div>
        </div>
        <div class="player-info">
            <h4>Attributes</h4>
            <div>
                <ul class="attributes-list">
                    <li>Strength: {player.strength}</li>
                    <li>Dexterity: {player.dexterity}</li>
                    <li>Charisma: {player.charisma}</li>
                    <li>Intelligence: {player.intelligence}</li>
                </ul>
            </div>
        </div>
    </div>
    """


def generate_html_midley(content):
    """
    Gera o conteúdo HTML para a caixa Midley Box.
    """
    formatted_content = "".join(f"<div>{item}</div>" for item in content)
    return f"""
    <h3>Midley Box</h3>
    <div>{formatted_content}</div>
    """


def generate_html_characters_present(content):
    """
    Gera o conteúdo HTML para a caixa Characters Present.
    """
    formatted_content = "".join(
        f"<div class='clickable-box' onclick=\"openCharacter('{item}')\">{item}</div>" for item in content
    )
    return f"""
    <div class="characters-container">{formatted_content}</div>
    """


def generate_html_map(mapa, player):
    """
    Gera o HTML para o quadrado do mapa.
    """
    url_casa = url_for('static', filename='img/icon/casa.png')
    url_rua = url_for('static', filename='img/icon/rua.png')

    mini_map = create_mini_map(mapa, player.local_id)
    formatted_content = ""
    for local in mini_map:
        block = f'<div class="map-inner-box"></div>'
        if local:
            block = f'<button class="map-inner-box" onclick="updateMap({local.id})">{local.id}</button>'

            # if local.nome == "rua":
            #     block = f'<button class="map-inner-box" onclick="updateMap({local.id})"><img class="local_id_{local.id}" src="{url_rua}" alt="icon rua"></button>'
            # else:
            #     block = f'<button class="map-inner-box" onclick="updateMap({local.id})"><img class="local_id_{local.id}" src="{url_casa}" alt="icon casa"></button>'

        formatted_content += block

    return f"""
    <div class="map-outer-box">
        {formatted_content}
    </div>
    """


@app.route("/take_damage", methods=["POST"])
def take_damage():
    dano = request.json.get("damage", 0)  # Obter o dano do corpo da requisição
    player.health = max(0, player.health - dano)  # Reduz a vida do jogador, garantindo que ela não fique negativa
    new_color = get_cor_vida(player.health)
    return jsonify({"health": player.health, "color": new_color})  # Retorna a nova vida em JSON

@app.route("/take_stamina_damage", methods=["POST"])
def take_stamina_damage():
    dano = request.json.get("damage", 0)  # Obter o dano do corpo da requisição
    player.stamina = max(0, player.stamina - dano)  # Reduz a vida do jogador, garantindo que ela não fique negativa
    new_color = get_stamina_color(player.stamina)
    return jsonify({"stamina": player.stamina, "color": new_color})  # Retorna a nova vida em JSON

@app.route("/update_map", methods=["POST"])
def update_map():
    local_id = request.json.get("local_id", 0)  # Obter o dano do corpo da requisição
    player.local_id = int(local_id)
    new_map = generate_html_map(mapa_gerado, player)
    return jsonify({"new-map":new_map})  # Retorna a nova vida em JSON

@app.route("/")
def index():
    # Conteúdo para os widgets
    midley_content = [f"Midley Item {i}" for i in range(10)]
    characters_content = [f"Character {i}" for i in range(50)]

    url_img = url_for('static', filename='img/test_img_player_200.png')

    # Geração dos HTMLs individuais
    player_status_html = generate_html_player_status([], player, url_img)
    midley_html = generate_html_midley(midley_content)
    characters_present_html = generate_html_characters_present(characters_content)

    map_html = generate_html_map(mapa_gerado, player)

    # Geração do HTML completo
    full_html = generate_full_html(player_status_html, midley_html, characters_present_html, map_html)
    return render_template_string(full_html)


if __name__ == "__main__":
    app.run(debug=True)
