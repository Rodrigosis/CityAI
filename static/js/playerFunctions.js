async function takeDamage(amount) {
    try {
        const response = await fetch("/take_damage", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ damage: amount }) // Enviar o dano como JSON
        });

        if (response.ok) {
            const data = await response.json(); // Obter a nova vida retornada pelo servidor
            const currentLife = data.health;

            const lifeBar = document.getElementById("player-life-bar");
            lifeBar.style.width = currentLife + "%";

            lifeBar.style.backgroundColor = data.color
        } else {
            console.error("Erro ao reduzir a vida do jogador:", response.statusText);
        }
    } catch (error) {
        console.error("Erro ao realizar a requisição:", error);
    }
}

async function takeStaminaDamage(amount) {
    try {
        const response = await fetch("/take_stamina_damage", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ damage: amount }) // Enviar o dano como JSON
        });

        if (response.ok) {
            const data = await response.json(); // Obter a nova vida retornada pelo servidor
            const currentStamina = data.stamina;

            const staminaBar = document.getElementById("player-stamina-bar");
            staminaBar.style.width = currentStamina + "%";

            staminaBar.style.backgroundColor = data.color
        } else {
            console.error("Erro ao reduzir a vida do jogador:", response.statusText);
        }
    } catch (error) {
        console.error("Erro ao realizar a requisição:", error);
    }
}

// Função para fazer POST e atualizar o mapa
function updateMap(localId) {
    // Fazer uma requisição POST usando fetch
    fetch('/update_map', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ local_id: localId }) // Enviando o local_id no corpo da requisição
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Erro ao atualizar o mapa');
        }
        return response.json(); // Parse do JSON retornado pelo servidor
    })
    .then(data => {
        // Substituir o conteúdo da 'map-outer-box' pelo novo HTML
        const mapOuterBox = document.querySelector('.map-outer-box');
        if (mapOuterBox && data['new-map']) {
            mapOuterBox.outerHTML = data['new-map'];
        }
    })
    .catch(error => {
        console.error('Erro ao realizar a requisição:', error);
    });
}