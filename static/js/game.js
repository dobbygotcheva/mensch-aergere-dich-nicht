// Don't b mad, man! - Game JavaScript
// Using real board positions from the hardware project (scaled from 150mm board to 600px SVG)

// Currency mapping for players
const currencyImages = {
    'red': '/static/images/dollar/cent1.png',
    'blue': '/static/images/euro/5cent.png',
    'green': '/static/images/leva/10st.png',
    'yellow': '/static/images/liri/5kr.jpg'
};

// Team piece images - each team has 4 unique pieces
const teamPieceImages = {
    'red': [
        '/static/images/team1/Leonardo.jpg',
        '/static/images/team1/raph.webp',
        '/static/images/team1/doni.jpeg',
        '/static/images/team1/mickey.png'
    ],
    'blue': [
        '/static/images/team2/hegel.jpeg',
        '/static/images/team2/karl marx.jpeg',
        '/static/images/team2/nietzsche.jpg',
        '/static/images/team2/Schopenhauer_by_Jules_Lunteschütz.jpg'
    ],
    'green': [
        '/static/images/team3/Beethoven.jpg',
        '/static/images/team3/liszt.jpg',
        '/static/images/team3/schumann.jpg',
        '/static/images/team3/todor_kolev.jpg'
    ],
    'yellow': [
        '/static/images/team4/bengal.jpg',
        '/static/images/team4/black.jpeg',
        '/static/images/team4/siberian_tiger.jpg',
        '/static/images/team4/white-tiger-Bengal.webp'
    ]
};

// Real positions from hardware project (SkaliranePozicije.txt)
// Scaled 4x from 150mm to 600px
const boardPositions = {
    // Main path positions (0-39) - outer circle
    0: {x: 225.68, y: 300.0},   // Red starting position
    1: {x: 182.52, y: 277.28},
    2: {x: 135.64, y: 246.76},
    3: {x: 91.64, y: 208.68},
    4: {x: 57.52, y: 164.56},
    5: {x: 40.0, y: 117.72},
    6: {x: 44.56, y: 74.4},
    7: {x: 74.64, y: 44.48},
    8: {x: 118.04, y: 40.04},
    9: {x: 164.92, y: 57.76},
    10: {x: 209.08, y: 92.0},   // Blue starting position
    11: {x: 247.16, y: 136.16},
    12: {x: 277.68, y: 183.16},
    13: {x: 300.0, y: 225.68},
    14: {x: 322.72, y: 182.52},
    15: {x: 353.24, y: 135.64},
    16: {x: 391.32, y: 91.64},
    17: {x: 435.44, y: 57.52},
    18: {x: 482.28, y: 40.0},
    19: {x: 525.6, y: 44.56},
    20: {x: 555.52, y: 74.64},   // Green starting position
    21: {x: 559.96, y: 118.04},
    22: {x: 542.24, y: 164.92},
    23: {x: 508.0, y: 209.08},
    24: {x: 463.84, y: 247.16},
    25: {x: 416.84, y: 277.68},
    26: {x: 374.32, y: 300.0},
    27: {x: 417.48, y: 322.72},
    28: {x: 464.36, y: 353.24},
    29: {x: 508.36, y: 391.32},
    30: {x: 542.48, y: 435.44},  // Yellow starting position
    31: {x: 560.0, y: 482.28},
    32: {x: 555.44, y: 525.6},
    33: {x: 525.36, y: 555.52},
    34: {x: 481.96, y: 559.96},
    35: {x: 435.08, y: 542.24},
    36: {x: 390.92, y: 508.0},
    37: {x: 352.84, y: 463.84},
    38: {x: 322.32, y: 416.84},
    39: {x: 300.0, y: 374.32},
    
    // Home lane positions (40-55) - paths to center
    // Red home lane (positions 53-56 in original, mapped to 40-43)
    40: {x: 135.52, y: 300.0},
    41: {x: 95.88, y: 260.36},
    42: {x: 95.88, y: 300.0},
    43: {x: 95.88, y: 339.64},
    
    // Blue home lane (positions 57-60 in original, mapped to 44-47)
    44: {x: 300.0, y: 135.52},
    45: {x: 339.64, y: 95.88},
    46: {x: 300.0, y: 95.88},
    47: {x: 260.36, y: 95.88},
    
    // Green home lane (positions 61-64 in original, mapped to 48-51)
    48: {x: 464.48, y: 300.0},
    49: {x: 504.12, y: 339.64},
    50: {x: 504.12, y: 300.0},
    51: {x: 504.12, y: 260.36},
    
    // Yellow home lane (positions 65-68 in original, mapped to 52-55)
    52: {x: 300.0, y: 464.48},
    53: {x: 260.36, y: 504.12},
    54: {x: 300.0, y: 504.12},
    55: {x: 339.64, y: 504.12},
    
    // Starting area positions (4 per player)
    // Red starting area (top-left) - positions 69-72
    '-1-red-0': {x: 200.92, y: 200.92},
    '-1-red-1': {x: 171.2, y: 171.2},
    '-1-red-2': {x: 141.48, y: 141.48},
    '-1-red-3': {x: 111.76, y: 111.76},
    
    // Blue starting area (top-right) - positions 73-76
    '-1-blue-0': {x: 399.08, y: 200.92},
    '-1-blue-1': {x: 428.8, y: 171.2},
    '-1-blue-2': {x: 458.52, y: 141.48},
    '-1-blue-3': {x: 488.24, y: 111.76},
    
    // Green starting area (bottom-right) - positions 77-80
    '-1-green-0': {x: 399.08, y: 399.08},
    '-1-green-1': {x: 428.8, y: 428.8},
    '-1-green-2': {x: 458.52, y: 458.52},
    '-1-green-3': {x: 488.24, y: 488.24},
    
    // Yellow starting area (bottom-left) - positions 81-84
    '-1-yellow-0': {x: 200.92, y: 399.08},
    '-1-yellow-1': {x: 171.2, y: 428.8},
    '-1-yellow-2': {x: 141.48, y: 458.52},
    '-1-yellow-3': {x: 111.76, y: 488.24},
};

// Initialize the board
function initializeBoard() {
    const piecesContainer = document.getElementById('pieces-container');
    piecesContainer.innerHTML = '';
    
    piecesData.forEach(piece => {
        createPieceElement(piece);
    });
}

// Create a piece element
function createPieceElement(piece) {
    const piecesContainer = document.getElementById('pieces-container');
    const pieceElement = document.createElement('div');
    pieceElement.className = `game-piece ${piece.player_color}`;
    pieceElement.id = `piece-${piece.id}`;
    pieceElement.dataset.pieceId = piece.id;
    
    // Use team character image as background
    if (piece.team_image) {
        pieceElement.style.backgroundImage = `url('/static/images/${piece.team_image}')`;
    } else {
        // Fallback to team images array if not in piece data
        const teamImages = teamPieceImages[piece.player_color];
        if (teamImages && teamImages[piece.piece_number]) {
            pieceElement.style.backgroundImage = `url('${teamImages[piece.piece_number]}')`;
        }
    }
    
    // Remove text label - image is enough
    // pieceElement.textContent = piece.piece_number + 1;
    
    // Get position
    let coords;
    if (piece.position === -1) {
        // In starting area
        const key = `-1-${piece.player_color}-${piece.piece_number}`;
        coords = boardPositions[key];
    } else {
        coords = boardPositions[piece.position];
    }
    
    if (coords) {
        const boardWidth = document.getElementById('game-board').clientWidth || 600;
        const scale = boardWidth / 600;
        pieceElement.style.left = `${coords.x * scale - 20}px`;
        pieceElement.style.top = `${coords.y * scale - 20}px`;
    }
    
    pieceElement.addEventListener('click', () => handlePieceClick(piece.id));
    piecesContainer.appendChild(pieceElement);
}

// Update piece position
function updatePiecePosition(pieceId, position, playerColor, pieceNumber) {
    const pieceElement = document.getElementById(`piece-${pieceId}`);
    if (!pieceElement) return;
    
    let coords;
    if (position === -1) {
        const key = `-1-${playerColor}-${pieceNumber}`;
        coords = boardPositions[key];
    } else {
        coords = boardPositions[position];
    }
    
    if (coords) {
        const boardWidth = document.getElementById('game-board').clientWidth || 600;
        const scale = boardWidth / 600;
        pieceElement.style.left = `${coords.x * scale - 20}px`;
        pieceElement.style.top = `${coords.y * scale - 20}px`;
    }
}

// Animate dice rolling by quickly changing images
function animateDiceRoll(finalValue, duration = 600) {
    const diceImage = document.getElementById('dice-image');
    const diceValueDisplay = document.getElementById('dice-value-display');
    
    // Hide value display during roll
    diceValueDisplay.classList.add('hidden');
    
    // Add rolling animation class
    diceImage.classList.add('rolling');
    
    // Rapidly change dice images
    const interval = 50; // Change image every 50ms
    const iterations = duration / interval;
    let currentIteration = 0;
    
    const rollInterval = setInterval(() => {
        const randomFace = Math.floor(Math.random() * 6) + 1;
        diceImage.src = `/static/images/dice/dice${randomFace}.png`;
        currentIteration++;
        
        if (currentIteration >= iterations) {
            clearInterval(rollInterval);
            // Show final result
            diceImage.src = `/static/images/dice/dice${finalValue}.png`;
            diceImage.classList.remove('rolling');
        }
    }, interval);
}

// Roll dice
async function rollDice() {
    const rollButton = document.getElementById('roll-button');
    const diceImage = document.getElementById('dice-image');
    const diceValueDisplay = document.getElementById('dice-value-display');
    
    rollButton.disabled = true;
    
    try {
        const response = await fetch(`/game/${gameId}/roll/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrfToken,
                'Content-Type': 'application/json',
            }
        });
        
        const data = await response.json();
        
        // Animate the dice roll
        animateDiceRoll(data.dice_value);
        
        setTimeout(() => {
            // Show final value
            diceValueDisplay.textContent = data.dice_value;
            diceValueDisplay.classList.remove('hidden');
            
            currentPlayerColor = data.current_player_color;
            movablePieces = data.movable_pieces;
            
            addLogMessage(`${data.current_player} rolled a ${data.dice_value}`);
            
            // Highlight movable pieces
            document.querySelectorAll('.game-piece').forEach(piece => {
                piece.classList.remove('movable');
            });
            
            movablePieces.forEach(pieceId => {
                const pieceElement = document.getElementById(`piece-${pieceId}`);
                if (pieceElement) {
                    pieceElement.classList.add('movable');
                }
            });
            
            if (movablePieces.length === 0) {
                addLogMessage('No valid moves available. Next turn!');
                setTimeout(() => {
                    fetch(`/game/${gameId}/state/`)
                        .then(res => res.json())
                        .then(state => {
                            updateCurrentPlayer(state.current_player, state.current_player_color);
                            diceValueDisplay.classList.add('hidden');
                            rollButton.disabled = false;
                        });
                }, 2000);
            }
        }, 650); // Wait for animation to complete
        
    } catch (error) {
        console.error('Error rolling dice:', error);
        diceImage.classList.remove('rolling');
        rollButton.disabled = false;
    }
}

// Handle piece click
async function handlePieceClick(pieceId) {
    if (!movablePieces.includes(pieceId)) {
        return;
    }
    
    try {
        const response = await fetch(`/game/${gameId}/move/${pieceId}/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrfToken,
                'Content-Type': 'application/json',
            }
        });
        
        const data = await response.json();
        
        if (data.success) {
            // Check for special task
            if (data.special_task) {
                showSpecialTask(data.special_task);
            }
            
            // Update all pieces
            data.all_pieces.forEach(piece => {
                const pieceData = piecesData.find(p => p.id === piece.id);
                if (pieceData) {
                    pieceData.position = piece.position;
                    pieceData.in_home = piece.in_home;
                }
                updatePiecePosition(piece.id, piece.position, piece.player_color, 
                                  pieceData ? pieceData.piece_number : 0);
            });
            
            // Clear movable highlights
            document.querySelectorAll('.game-piece').forEach(piece => {
                piece.classList.remove('movable');
            });
            
            movablePieces = [];
            
            if (data.game_over) {
                showWinnerModal(data.winner);
            } else {
                updateCurrentPlayer(data.next_player, data.next_player_color);
                addLogMessage(`Piece moved! ${data.next_player}'s turn.`);
                
                // Reset dice
                const diceValueDisplay = document.getElementById('dice-value-display');
                if (diceValueDisplay) {
                    diceValueDisplay.classList.add('hidden');
                }
                
                // Enable roll button
                document.getElementById('roll-button').disabled = false;
            }
        }
    } catch (error) {
        console.error('Error moving piece:', error);
    }
}

// Update current player display
function updateCurrentPlayer(playerName, playerColor) {
    document.getElementById('current-player-name').textContent = playerName;
    const turnBadge = document.querySelector('.player-turn-badge');
    turnBadge.style.background = `var(--color-${playerColor})`;
    
    // Highlight active player card
    document.querySelectorAll('.player-card').forEach(card => {
        card.classList.remove('active');
    });
    document.getElementById(`player-card-${playerColor}`)?.classList.add('active');
    
    currentPlayerColor = playerColor;
}

// Add log message
function addLogMessage(message) {
    const logMessages = document.getElementById('log-messages');
    const messageElement = document.createElement('p');
    messageElement.className = 'log-message';
    messageElement.textContent = message;
    logMessages.insertBefore(messageElement, logMessages.firstChild);
    
    // Keep only last 10 messages
    while (logMessages.children.length > 10) {
        logMessages.removeChild(logMessages.lastChild);
    }
}

// Show winner modal
function showWinnerModal(winnerName) {
    const modal = document.getElementById('winner-modal');
    document.getElementById('winner-name').textContent = winnerName;
    modal.classList.add('show');
    addLogMessage(`🎉 ${winnerName} wins the game! 🎉`);
}

// Show special task modal
function showSpecialTask(task) {
    // Create modal overlay
    const overlay = document.createElement('div');
    overlay.className = 'task-modal-overlay';
    
    // Build image HTML if image exists
    const imageHTML = task.image ? 
        `<div class="task-image"><img src="/static/images/${task.image}" alt="${task.title}"></div>` : 
        `<div class="task-icon">${getTaskIcon(task.type)}</div>`;
    
    overlay.innerHTML = `
        <div class="task-modal">
            <div class="task-header ${getTaskTypeClass(task.type)}">
                <h2>${task.title}</h2>
                <span class="task-type-badge">${task.type.toUpperCase()}</span>
            </div>
            <div class="task-body">
                ${imageHTML}
                <p class="task-description">${task.task}</p>
            </div>
            <button class="task-close-btn" onclick="this.closest('.task-modal-overlay').remove()">
                Got it! ✓
            </button>
        </div>
    `;
    document.body.appendChild(overlay);
    
    // Auto-close after 15 seconds (longer for reading challenges)
    setTimeout(() => {
        if (overlay.parentElement) {
            overlay.remove();
        }
    }, 15000);
}

function getTaskTypeClass(type) {
    const classes = {
        'knowledge': 'task-knowledge',
        'bonus': 'task-bonus',
        'choice': 'task-choice',
        'challenge': 'task-challenge',
        'penalty': 'task-penalty',
        'special': 'task-special',
        'attack': 'task-attack'
    };
    return classes[type] || 'task-default';
}

function getTaskIcon(type) {
    const icons = {
        'knowledge': '🧠',
        'bonus': '🎁',
        'choice': '🤔',
        'challenge': '⚡',
        'penalty': '⚠️',
        'special': '✨',
        'attack': '⚔️'
    };
    return icons[type] || '🎲';
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
    initializeBoard();
    
    // Highlight current player
    const currentCard = document.getElementById(`player-card-${currentPlayerColor}`);
    if (currentCard) {
        currentCard.classList.add('active');
    }
    
    // Handle window resize
    window.addEventListener('resize', () => {
        piecesData.forEach(piece => {
            updatePiecePosition(piece.id, piece.position, piece.player_color, piece.piece_number);
        });
    });
});

