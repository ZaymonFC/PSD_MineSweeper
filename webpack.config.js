module.exports = {
    entry: "./js/__entrypoint.js",
    output: {
        filename: './js/output.js'
    },
    resolve: {
        extensions: ['.js']
    },
    devtool: 'source-map'
}