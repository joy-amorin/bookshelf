const path = require('path');

module.exports = {
  entry: './src/index.js',
  output: {
    path: path.resolve(__dirname, 'static/frontend'),
    filename: 'main.js',
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
        },
      },
      {
        test: /\.css$/, // Regla para manejar archivos CSS
        use: ['style-loader', 'css-loader'], // Carga los estilos en el DOM y procesa los archivos CSS
      },
    ],
  },
  resolve: {
    extensions: ['*', '.js', '.jsx'],
  },
  devServer: {
    static: path.join(__dirname, 'static/frontend'),
    compress: true,
    port: 3000,
    historyApiFallback: true,
  },
};
