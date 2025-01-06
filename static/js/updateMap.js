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