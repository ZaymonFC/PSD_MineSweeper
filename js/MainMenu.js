import Phaser from './phaser.min.js'

import { BGCOLOUR } from './GameConfig'

export default class MainMenu extends Phaser.State {

    preload() {
        this.load.image('title', '/assets/Title.svg')
    }

    create() {
        this.stage.backgroundColor = BGCOLOUR
        this.add.sprite(55, 60, 'title')
    }

    update() {

    }
}