const webpack = require("webpack");

module.exports = {
  publicPath: "/ner-annotator/",
  outputDir: "./docs/",

  chainWebpack: config => {
    config.module
      .rule('raw')
      .test(/\.txt$/)
      .use('raw-loader')
      .loader('raw-loader')
      .end();
  },

  pluginOptions: {
    quasar: {
      importStrategy: "kebab",
      rtlSupport: false,
    },
  },

  configureWebpack: (config) => {
    return {
      plugins: [
        new webpack.DefinePlugin({
          APPLICATION_VERSION: JSON.stringify(
            require("./package.json").version
          ),
        }),
      ],
    };
  },

  transpileDependencies: ["quasar"],
};
