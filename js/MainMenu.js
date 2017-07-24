import Phaser from './phaser.min.js'

import { BGCOLOUR } from './GameConfig'

export default class MainMenu extends Phaser.State {

    preload() {
        this.load.image('title', '/assets/Title.svg')
        this.load.image('stdBtn', '/assets/stdBtn.svg')
        this.load.image('hexBtn', '/assets/hexBtn.svg')
        this.load.image('highscoreBtn', '/assets/highscoreBtn.svg')

    }

    create() {
        this.stage.backgroundColor = BGCOLOUR
        let titlebar = this.add.sprite(this.world.centerX, 100, 'title').anchor.setTo(0.5, 0.5)

        // Buttons
        let stdBtn = this.add.button(this.world.centerX + 0.5, 320.5, 'stdBtn', this.stdBtnClick)
            .anchor.setTo(0.5, 0.5)
        let hexBtn = this.add.button(this.world.centerX + 0.5, 400.5, 'hexBtn', this.stdBtnClick)
            .anchor.setTo(0.5, 0.5)
        let highscoreBtn = this.add.button(this.world.centerX + 0.5, 480.5, 'highscoreBtn', this.stdBtnClick)
            .anchor.setTo(0.5, 0.5)
    }

    update() {

    }

    /* 
    ** Event Handlers
    */
    stdBtnClick() {
        this.game.state.start('GameState')
    }

    hexBtnClick(){
        
    }

    highscoreBtnClick(){
        
    }

}