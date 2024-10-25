const path = require('path');

module.exports = {
    entry: ['./assets/scripts/index.js'],
    output: {
      filename: 'bundle.js',
      path: path.resolve(__dirname, '../authentication/', 'static'),
    },
    module: {
        rules: [
            {
                test: /\.css$/,
                use: ['style-loader', 'css-loader'],
            }
        ]        
    }
  };