import Phaser from './phaser.min.js'
import MainMenu from './MainMenu'
import GameState from './GameState'


let conf = {
    height: 720,
    width: 720
}

export default class MineSweeper extends Phaser.Game{
    constructor(){
        super(conf.height, conf.width, Phaser.AUTO, '')
        // Load the menu game state
        //let mainMenu = new MainMenu(this.game)
        //let gameState = new GameState(game)
        this.state.add('GameState', GameState)
        this.state.add('Main Menu', MainMenu)
        this.state.start('GameState')
    }
    
    updateState(){

    }
}