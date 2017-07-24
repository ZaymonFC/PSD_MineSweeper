import Phaser from './phaser.min.js'

let gameConf = {
    boardHeight: 10,
    boardWidth: 10,
    mineCount: 10,
    tileDimension: 46,
    edgeOffset: 10
}


export default class GameState extends Phaser.State {

    constructor() {
        super()
        game: Phaser.game
        this.preload(this.game)
        this.create()
    }

    // Shift assets to memory
    preload(game) {
        // Load the Square tileset

        game.load.image('tile', '../assets/square tile.svg')

        // Load the hexagonal tileset

    }
    // Create elements
    create() {
        // Set the stage
        game.stage.backgroundColor = "F19C79"
        // Create the grid

        var grid = makeGrid();
        game.add.group(grid);

        // Populate the mines

        // Start Scoring

        // Handle clicks

    }

    makeGrid() {
        grid = this.game.add.group()
        for (var i = 0; i < gameConf.boardHeight; i++) {
            for (var j = 0; j < gameConf.boardWidth; j++) {
                grid.create(j * gameConf.tileDimension + gameConf.edgeOffset,
                    i * gameConf.tileDimension + gameConf.edgeOffset, 'tile');
            }
        }
        return grid
    }
}

