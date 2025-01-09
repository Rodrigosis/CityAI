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