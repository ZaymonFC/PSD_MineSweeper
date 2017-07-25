import Phaser from './phaser.min.js'
import { BOARDHEIGHT, BOARDWIDTH, TILEDIMENSION, EDGEOFFSET, BGCOLOUR } from './GameConfig'

let images = {
    square_up: "assets/square_up.svg",
    square_down: "assets/",
    square_bomb: "assets/",
    square_covered: "assets/",
    hex_up: "assets/",
    hex_down: "assets/",
    hex_bomb: "assets/",
    hex_covered: "assets/"
}


export default class GameState extends Phaser.State {
    preload() {
        // Load the frame boarder
        this.load.image('frameBoarder', '/assets/outerStroke.svg')  
        
        
        // Load buttons
        this.load.image('tile', '../assets/Square Tile.svg')

    }

    create() {
        // Set the stage
        this.stage.backgroundColor = BGCOLOUR
        let frameBoarder = this.add.sprite(0,0, 'frameBoarder')
        // Create the grid

        this.grid = this.makeGrid()
        this.add.group(this.grid)
    }

    update() {

    }

    makeGrid() {
        let grid = this.add.group()
        for (var i = 0; i < BOARDHEIGHT; i++) {
            for (var j = 0; j < BOARDWIDTH; j++) {
                grid.create(j * TILEDIMENSION + EDGEOFFSET,
                    i * TILEDIMENSION + EDGEOFFSET, 'tile')
            }
        }
        return grid
    }
}