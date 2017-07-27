import Phaser from './phaser.min.js'
import { BOARDHEIGHT, BOARDWIDTH, TILEDIMENSION, EDGEOFFSET, BGCOLOUR } from './GameConfig'
import GameTile from './GameTile'


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
        this.load.spritesheet('square_tile', '/assets/spriteSheets/sqrSpriteSheet.png', 95, 98, 4)
    }

    create() {
        // Set the stage
        this.stage.backgroundColor = BGCOLOUR
        let frameBoarder = this.add.sprite(0,0, 'frameBoarder')
        // Create the grid

        // let grid = this.makeGrid()
        // this.add.group(this.grid)

        // Create an adjacency list representation of the board
        // let graph = this.createGraph();
        // console.log(graph[0])

        //Create an array of mines
        let mines = this.makeGrid();
    }

    update() {

    }

    // New Makegrid function
    makeGrid(){
        // Create a group
        let grid = this.add.group()
        for (var i = 0; i < BOARDHEIGHT; i++){
            for (var j = 0; j < BOARDWIDTH; j++){
                let button = new GameTile(this.game, j * TILEDIMENSION + EDGEOFFSET, i * TILEDIMENSION + EDGEOFFSET, 'square_tile', i, j)
                grid.add(button)
            }
        }
        return grid
    }

    
    createGraph(){
        let graph = {}
        let w = BOARDWIDTH
        let h = BOARDHEIGHT

        for (var i = 0; i < w; i++){
            let array = new Array()
            for (var j = 0; j < h; j++){
                // Top left
                if (i - 1 > 0 && j - 1 > 0){
                    array.push([i,j])
                }
                // Top
                if (i - 1 < 0){
                    array.push([i,j])
                }
                // Top Right
                if (i - 1 < 0 && j + 1 < w){
                    array.push([i,j])
                }
                // Right
                if (j + 1 < w){
                    array.push([i,j])
                }
                // Bottom Right
                if (i + 1 < h && j + 1 < w){
                    array.push([i,j])
                }
                // Bottom
                if (i + 1 < h){
                    array.push([i,j])
                }
                // Bottom Left
                if (i + 1 < h && j - 1 > 0){
                    array.push([i,j])
                }
                // Left
                if (j -1 > 0){
                    array.push([i,j])  
                }
                graph[i * h + j] = array
            }
        }
        return graph
    }

    createMines(){
        return 0
    }
    




    // makeGrid() {
    //     let grid = this.add.group()
    //     for (var i = 0; i < BOARDHEIGHT; i++) {
    //         for (var j = 0; j < BOARDWIDTH; j++) {
    //             grid.create(j * TILEDIMENSION + EDGEOFFSET,
    //                 i * TILEDIMENSION + EDGEOFFSET, 'tile')
    //         }
    //     }
    //     return grid
    // }
}