// game.js
let board = [];
let moves = 0;
let remainingMoves = 0;
let rows = 4;
let cols = 4;
let gameStarted = false;

function createBoard(r, c) {
    board = [];
    let num = 1;
    for (let i = 0; i < r; i++) {
        let row = [];
        for (let j = 0; j < c; j++) {
            if (i === r - 1 && j === c - 1) {
                row.push(" ");
            } else {
                row.push(num++);
            }
        }
        board.push(row);
    }
    return board;
}

function findEmpty() {
    for (let i = 0; i < board.length; i++) {
        for (let j = 0; j < board[0].length; j++) {
            if (board[i][j] === " ") {
                return [i, j];
            }
        }
    }
}

function moveRight() {
    let [row, col] = findEmpty();
    if (col > 0) {
        [board[row][col], board[row][col - 1]] = [board[row][col - 1], board[row][col]];
    } else {
        // Wrap to end of row
        [board[row][col], board[row][board[0].length - 1]] = [board[row][board[0].length - 1], board[row][col]];
    }
    return true;
}

function moveLeft() {
    let [row, col] = findEmpty();
    if (col < board[0].length - 1) {
        [board[row][col], board[row][col + 1]] = [board[row][col + 1], board[row][col]];
    } else {
        // Wrap to start of row
        [board[row][col], board[row][0]] = [board[row][0], board[row][col]];
    }
    return true;
}

function moveUp() {
    let [row, col] = findEmpty();
    if (row > 0) {
        [board[row][col], board[row - 1][col]] = [board[row - 1][col], board[row][col]];
    } else {
        // Wrap to bottom
        [board[row][col], board[board.length - 1][col]] = [board[board.length - 1][col], board[row][col]];
    }
    return true;
}

function moveDown() {
    let [row, col] = findEmpty();
    if (row < board.length - 1) {
        [board[row][col], board[row + 1][col]] = [board[row + 1][col], board[row][col]];
    } else {
        // Wrap to top
        [board[row][col], board[0][col]] = [board[0][col], board[row][col]];
    }
    return true;
}

function updateBoard() {
    const boardElement = document.getElementById('board');
    boardElement.style.gridTemplateColumns = `repeat(${cols}, 1fr)`;
    boardElement.innerHTML = '';

    for (let i = 0; i < board.length; i++) {
        for (let j = 0; j < board[0].length; j++) {
            const tile = document.createElement('div');
            tile.className = 'tile' + (board[i][j] === " " ? ' empty' : '');
            tile.textContent = board[i][j];
            boardElement.appendChild(tile);
        }
    }

    if (gameStarted) {
        moves++;
        remainingMoves--;
        document.getElementById('moves').textContent = moves;
        document.getElementById('remaining').textContent = remainingMoves;

        if (remainingMoves <= 0) {
            gameStarted = false;
            alert('Game Over - No moves remaining!');
            resetGame();
        } else if (isWin()) {
            gameStarted = false;
            alert('Congratulations! You won!');
            resetGame();
        }
    }
}

function isWin() {
    let num = 1;
    for (let i = 0; i < board.length; i++) {
        for (let j = 0; j < board[0].length; j++) {
            if (i === board.length - 1 && j === board[0].length - 1) {
                return board[i][j] === " ";
            }
            if (board[i][j] !== num++) {
                return false;
            }
        }
    }
    return true;
}

function shuffleBoard() {
    const shuffleMoves = rows * cols * 20;
    const moves = ['moveUp', 'moveDown', 'moveLeft', 'moveRight'];
    let lastMove = '';

    for (let i = 0; i < shuffleMoves; i++) {
        let possibleMoves = moves.filter(move => {
            if ((lastMove === 'moveUp' && move === 'moveDown') ||
                (lastMove === 'moveDown' && move === 'moveUp') ||
                (lastMove === 'moveLeft' && move === 'moveRight') ||
                (lastMove === 'moveRight' && move === 'moveLeft')) {
                return false;
            }
            return window[move]();
        });

        if (possibleMoves.length > 0) {
            const randomMove = possibleMoves[Math.floor(Math.random() * possibleMoves.length)];
            window[randomMove]();
            lastMove = randomMove;
        }
    }
}

function startGame() {
    rows = parseInt(document.getElementById('rows').value);
    cols = parseInt(document.getElementById('cols').value);

    if (rows < 2 || rows > 15 || cols < 2 || cols > 15) {
        alert('Please enter valid dimensions (2-15)');
        return;
    }

    board = createBoard(rows, cols);
    moves = 0;
    remainingMoves = rows * cols * 5;

    shuffleBoard();
    gameStarted = true;

    document.getElementById('moves').textContent = '0';
    document.getElementById('remaining').textContent = remainingMoves;
    updateBoard();
}

function resetGame() {
    gameStarted = false;
    startGame();
}

function handleMove(direction) {
    if (!gameStarted) return;

    switch(direction) {
        case 'w': moveUp(); break;
        case 's': moveDown(); break;
        case 'a': moveLeft(); break;
        case 'd': moveRight(); break;
        default: return;
    }

    updateBoard();
    event.preventDefault();
}

document.addEventListener('keydown', (e) => {
    if (!gameStarted) return;

    switch(e.key.toLowerCase()) {
        case 'w': moveUp(); break;
        case 's': moveDown(); break;
        case 'a': moveLeft(); break;
        case 'd': moveRight(); break;
        default: return;
    }

    updateBoard();
});

// Initialize game on load
window.onload = startGame;