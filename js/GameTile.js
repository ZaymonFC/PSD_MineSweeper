
import Phaser from './phaser.min.js'

export default class GameTile extends Phaser.Button{
    constructor(game, x, y, key, i, j){
        super(game, x, y, key)
        this.key = key
        this.game = game
        this.x = x
        this.y = y
        this.i = i
        this.j = j
        this.anchor.setTo(0.5, 0.5)
        


        this.inputEnabled = true;
        this.input.useHandCursor = true;
        this.events.onInputOut.add(this.rollOut, this);
        this.events.onInputOver.add(this.rollOver, this);
        this.marked = false;

    }
    
    
    setMine(){

    }

    checkMine(){

    }

    over(){

    }

    out(){

    }

    actionOnClick(){

    }

    actionOnHold(){

    }


}



// export default class Tile {


//     constructor(gameRef, x, y, type, i, j) {
//         // Store the different images in a variable
//         this.svgs = {
//             square_up: "assets/square_up.svg",
//             square_down: "assets/",
//             square_bomb: "assets/",
//             square_covered: "assets/",
//             hex_up: "assets/",
//             hex_down: "assets/",
//             hex_bomb: "assets/",
//             hex_covered: "assets/",
//         }
//         this.anchor.setTo(0.5, 0.5)
//         this.tileText = game.make.text(0, 0, type)

//         this.tileText.anchor.setTo(0.5, 0.5)
//         this.tileText.addColor('#F6F4D2', 0)
//     }


// }