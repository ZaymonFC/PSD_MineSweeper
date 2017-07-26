import Phaser from './phaser.min.js'
import MainMenu from './MainMenu'
import GameState from './GameState'

import { WIDTH, HEIGHT } from './GameConfig'


export default class MineSweeper extends Phaser.Game{
    constructor(){
        super(HEIGHT, WIDTH, Phaser.AUTO, '')
        // Load the menu game state
        //let mainMenu = new MainMenu(this.game)
        //let gameState = new GameState(game)
        this.state.add('GameState', GameState)
        this.state.add('MainMenu', MainMenu)
        //this.state.start('MainMenu')
        this.state.start('GameState')
    }
    
    updateState(){

    }
}