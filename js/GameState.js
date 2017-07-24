import Phaser from './phaser.min.js'

let gameConf = {
    boardHeight: 10,
    boardWidth: 10,
    mineCount: 10,
    tileDimension: 46,
    edgeOffset: 10
}

export default class GameState extends Phaser.State {
    preload(){
        this.game.load.image('tile', '../assets/square tile.svg')
    }

    create(){
        this.stage.backgroundColor = "F19C79"
        // Create the grid

        this.grid = this.makeGrid();
        this.add.group(this.grid);
    }

    update(){

    }

    makeGrid() {
        let grid = this.add.group()
        for (var i = 0; i < gameConf.boardHeight; i++) {
            for (var j = 0; j < gameConf.boardWidth; j++) {
                grid.create(j * gameConf.tileDimension + gameConf.edgeOffset,
                    i * gameConf.tileDimension + gameConf.edgeOffset, 'tile');
            }
        }
        return grid
    }
}