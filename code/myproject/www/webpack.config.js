const path = require('path');

module.exports = {
    entry: {
      main: ['./assets/scripts/index.js'],  
      signup: ['./assets/scripts/signup.bundle.js'],
    }, 
    output: {
      filename: '[name].bundle.js',
      path: path.resolve(__dirname, '../authentication/', 'static'),
    },
    module: {
        rules: [
            {
                test: /\.css$/i,
                use: ['style-loader', 'css-loader'],
            }
        ]        
    }
  };