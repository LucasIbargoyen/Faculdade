let minedCount = 0;

document.addEventListener('DOMContentLoaded', (event) => {
    let campoMinado = document.getElementById('campoMinado');

    if (campoMinado) {
        campoMinado.textContent = "";  // Limpa o conteúdo existente

        // Criar um tabuleiro 10x10
        for (let i = 0; i < 10; i++) {
            for (let j = 0; j < 10; j++) {
                let cell = document.createElement('div');
                cell.className = 'cell';
                cell.dataset.row = i;
                cell.dataset.col = j;
                cell.addEventListener('click', () => makeMove(i, j));  // Adicionar evento de clique
                campoMinado.appendChild(cell);
            }
        }
    } else {
        console.error("Elemento 'campoMinado' não encontrado.");
    }
});

function makeMove(row, col) {
    fetch('/make_move', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ row: row, col: col })
    }).then(response => response.json()).then(data => {
        const cell = document.querySelector(`div[data-row="${row}"][data-col="${col}"]`);
        if (cell) {
            cell.textContent = data.result;
            if (data.result === "Game Over") {
                cell.className = "cell mine";
                minedCount++;
                if (minedCount >= 3) {
                    alert("Game Over! Você selecionou 3 blocos minados.");
                    disableBoard();
                }
            } else {
                cell.className = "cell safe";
            }
        }
    });
}

function disableBoard() {
    let cells = document.querySelectorAll('.cell');
    cells.forEach(cell => cell.removeEventListener('click', makeMove));
}
