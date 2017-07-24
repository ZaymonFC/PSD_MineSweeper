export default class Tile {


    constructor(gameRef, x, y, type, i, j) {
        // Store the different images in a variable
        this.svgs = {
            square_up: "assets/square_up.svg",
            square_down: "assets/",
            square_bomb: "assets/",
            square_covered: "assets/",
            hex_up: "assets/",
            hex_down: "assets/",
            hex_bomb: "assets/",
            hex_covered: "assets/",
        }
        this.anchor.setTo(0.5, 0.5)
        this.tileText = game.make.text(0, 0, type)

        this.tileText.anchor.setTo(0.5, 0.5)
        this.tileText.addColor('#F6F4D2', 0)
    }


}