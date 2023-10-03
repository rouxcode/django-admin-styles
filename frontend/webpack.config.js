const path = require("path")
const CopyPlugin = require("copy-webpack-plugin")
const MiniCssExtractPlugin = require("mini-css-extract-plugin")

const root = path.resolve(__dirname, '../admin_styles')
const source = path.resolve(__dirname, "admin_styles")
const targets = {
    prod: path.resolve(root, "static"),
    dev: path.resolve(root, "static_dev")
}


// webpack entry points -------------------------------------------------------

module.exports = (env, argv) => {

    const is_prod = argv.mode === "production"
    const target = is_prod ? targets['prod'] : targets['dev']
    const copies = [
        { from: source + '/imgs', to: target + '/admin_styles/imgs' },
    ]

    return [

        // project assets ---------------------------------------------------------
        {
            entry: { 'admin_styles/admin': path.resolve(source, "admin.js") },
            resolve: get_resolve(),
            output: get_output(target),
            plugins: get_plugins(copies),
            module: {
                rules: [
                    get_css_rule(),
                    get_file_rule(source)
                ],
            },
        },
    ]

    function get_css_rule() {
        return {
            // sass/scss compiler
            test: /\.scss$/i,
            use: [
                MiniCssExtractPlugin.loader,
                "css-loader",
                "sass-loader",
            ],
        }
    }

    function get_file_rule(source) {
        // file handler
        return {
            test: /\.(svg|png|jpg|gif|webp|eot|woff|woff2|ttf|otf|ico)$/,
            exclude: /node_modules/,
            use: {
                loader: 'file-loader',
                options: {
                    context: source,
                    name: '[path][name].[ext]'
                }
            }
        }
    }

    function get_output(destination) {
        return {
            path: destination,
            filename: "[name].js",
        }
    }

    function get_plugins(copy_patterns) {
        const plugins = [new MiniCssExtractPlugin()]
        if (copy_patterns) {
            plugins.push(new CopyPlugin({ patterns: copy_patterns }))
        }
        return plugins
    }

    function get_resolve() {
        const node_modules = path.resolve(__dirname, 'node_modules');
        return {
            // add custom  node_modules import path
            modules: [node_modules, 'node_modules'],
        }
    }
}
