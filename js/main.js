window.onload = function () {

    // Define a config variable to store configurable properties
    var gameConf = {
        height: 800,
        width: 600,
        boardHeight: 10,
        boardWidth: 10,
        mineCount: 10,
        tileDimension: 46,
        edgeOffset: 10
    }

    var game = new Phaser.Game(gameConf.height, gameConf.width, Phaser.AUTO, '')



    var gameState = {

        // Shift assets to memory
        preload: function () {
            // Load the Square tileset
            game.load.image('tile', 'assets/square tile.svg')

            // Load the hexagonal tileset

        },

        // Create elements
        create: function () {
            // Set the stage
            game.stage.backgroundColor = "F19C79"
            // Create the grid
            
            var grid = makeGrid();
            game.add.group(grid);

            // Populate the mines

            // Start Scoring

            // Handle clicks
            
        }
    }

    function makeGrid() {
        grid = game.add.group()
        for (var i = 0; i < gameConf.boardHeight; i++) {
            for (var j = 0; j < gameConf.boardWidth; j++) {
                grid.create(j * gameConf.tileDimension + gameConf.edgeOffset, i * gameConf.tileDimension + gameConf.edgeOffset, 'tile');
            }
        }
        return grid
    }


    // Run the initial gamestate

    // Main Menu


    game.state.add('Game', gameState)
    game.state.start('Game')
};
