import Phaser from './phaser.min.js'
import { BOARDHEIGHT, BOARDWIDTH, TILEDIMENSION, EDGEOFFSET, BGCOLOUR } from './GameConfig'

export default class GameState extends Phaser.State {
    preload() {
        this.load.image('tile', '../assets/square tile.svg')
    }

    create() {
        this.stage.backgroundColor = BGCOLOUR
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