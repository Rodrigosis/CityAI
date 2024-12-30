from flask import Flask, render_template_string, render_template, url_for

app = Flask(__name__)


def generate_full_html(player_status_html, midley_html, characters_present_html, map_html):
    """
    Gera o HTML contendo todas as 4 caixas no layout em grid.
    """
    return f"""
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #2e2e2e;
                color: white;
                display: grid;
                grid-template-columns: 2fr 3fr 2fr;
                grid-template-rows: 3fr 2fr;
                gap: 1rem;
                height: 100vh;
            }}
            .box {{
                background-color: #303030;
                border: 2px solid #555;
                border-radius: 8px;
                padding: 10px;
                overflow: auto;
            }}
            .map-box {{
                background-color: white;
                color: black;
                font-weight: bold;
                display: flex;
                justify-content: center;
                align-items: center;
            }}

            /* Estilo das barras de scroll */
            .box::-webkit-scrollbar {{
                width: 10px;
                height: 10px;
            }}
            .box::-webkit-scrollbar-thumb {{
                background-color: #5e5e5e;
                border-radius: 10px;
                border: 2px solid #303030;
            }}
            .box::-webkit-scrollbar-thumb:hover {{
                background-color: #787878;
            }}
            .box::-webkit-scrollbar-track {{
                background-color: #404040;
                border-radius: 10px;
            }}

            /* Estilo do botão */
            .damage-button {{
                margin-top: 15px;
                padding: 10px 15px;
                background-color: #ff0000;
                color: white;
                border: 1px solid #222;
                border-radius: 5px;
                font-size: 16px;
                cursor: pointer;
            }}
            .damage-button:hover {{
                background-color: #cc0000;
            }}
        </style>
        <script>
            let currentLife = 75;

            function takeDamage(amount) {{
                currentLife = Math.max(0, currentLife - amount);
                const lifeBar = document.getElementById("player-life-bar");
                lifeBar.style.width = currentLife + "%";

                if (currentLife > 50) {{
                    lifeBar.style.backgroundColor = "#00FF00";
                }} else if (currentLife > 20) {{
                    lifeBar.style.backgroundColor = "#FFFF00";
                }} else {{
                    lifeBar.style.backgroundColor = "#FF0000";
                }}

                lifeBar.title = `Vida Atual: $currentLife%`;
            }}
        </script>
    </head>
    <body>
        <div class="box" style="grid-column: 1; grid-row: span 2;">
            <h3>Player Status</h3>
            {player_status_html}
        </div>
        <div class="box" style="grid-column: 2; grid-row: span 2;">
            <h3>Midley Box</h3>
            {midley_html}
            <button class="damage-button" onclick="takeDamage(10)">Tomar Dano (-10)</button>
        </div>
        <div class="box" style="grid-column: 3; grid-row: 1;">
            <h3>Characters Present</h3>
            {characters_present_html}
        </div>
        <div class="box map-box" style="grid-column: 3; grid-row: 2;">
            <h3>Mapa</h3>
            {map_html}
        </div>
    </body>
    </html>
    """


def generate_html_player_status(content, vida, url_img):
    """
    Gera o conteúdo HTML para a caixa Player Status com uma barra de vida.
    """
    formatted_content = "".join(
        f"<div class='player-text'>{item}</div>" for item in content
    )
    # <img src="Users/rodri/vs_code/CityAI/img/test_img_player_200.png" "style=width: 100%; height: 200px; object-fit: contain;">
    return f"""
    <div class="player-box">
        <div class="player-image">
            <img src="{url_img}" alt="Imagem do jogador">
        </div>
        {formatted_content}
        <div 
            class="vida-bar" 
            style="width: 100%; height: 20px; background-color: #555; border: 1px solid #333; border-radius: 5px; margin-top: 10px; overflow: hidden;">
            <div 
                id="player-life-bar"
                title="Vida Atual: {vida}%" 
                style="width: {vida}%; height: 100%; background-color: {get_cor_vida(vida)};">
            </div>
        </div>
    </div>
    """


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


def generate_html_midley(content):
    """
    Gera o conteúdo HTML para a caixa Midley Box.
    """
    formatted_content = "".join(f"<div>{item}</div>" for item in content)
    return f"<div>{formatted_content}</div>"


def generate_html_characters_present(content):
    """
    Gera o conteúdo HTML para a caixa Characters Present.
    """
    formatted_content = "".join(f"<div>{item}</div>" for item in content)
    return f"<div>{formatted_content}</div>"


def generate_html_map():
    """
    Gera o HTML para o quadrado do mapa.
    """
    return "<div>Mapa do Jogo</div>"


@app.route("/")
def index():
    # Conteúdo do Player Status
    player_status_content = ["Nivel: 10", "XP: 1500/2000", "Classe: Guerreiro"]
    vida = 75

    # Conteúdo para os widgets
    midley_content = [f"Midley Item {i}" for i in range(10)]
    characters_content = [f"Character {i}" for i in range(5)]
    map_content = "Este é o mapa"

    url_img = url_for('static', filename='img/test_img_player_200.png')

    # Geração dos HTMLs individuais
    player_status_html = generate_html_player_status(player_status_content, vida, url_img)
    midley_html = generate_html_midley(midley_content)
    characters_present_html = generate_html_characters_present(characters_content)
    map_html = generate_html_map()

    # Geração do HTML completo
    full_html = generate_full_html(player_status_html, midley_html, characters_present_html, map_html)
    return render_template_string(full_html)


if __name__ == "__main__":
    app.run(debug=True)
