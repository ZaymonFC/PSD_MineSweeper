export default class Tile {
    constructor (gameRef, x, y, tileSvg, type, i, j) {
        this.anchor.setTo(0.5, 0.5)
        this.tileText = game.make.text(0, 0, type)

        this.tileText.anchor.setTo(0.5, 0.5)
        this.tileText.addColor('#F6F4D2', 0)
    }


}