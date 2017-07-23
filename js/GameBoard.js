var GameBoard = function (columns, rows, gameType) {
    var board = []
    var group = game.add.group()

    if (gameType == 'sqr') {
        for (var i = 0; i < rows; i++) {
            var row = []

            // Add tiles to each row
            for (var j = 0; j < columns; j++) {
                var tile = new Tile(i, j, group)
                // Push the tile to the row
                row.push(tile)
            }

            // Push the row to the board
            board.push(row)
        }
    }

}