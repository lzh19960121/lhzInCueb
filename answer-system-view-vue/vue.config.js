module.exports = {
    // baseUrl从 Vue CLI 3.3 起已弃用，请使用publicPath
    // 默认情况下，Vue CLI 会假设你的应用是被部署在一个域名的根路径上，例如 https://www.my-app.com/。
    // 如果应用被部署在一个子路径上，你就需要用这个选项指定这个子路径。例如，如果你的应用被部署在 https://www.my-app.com/my-app/，则设置 publicPath 为 /my-app/。
    // 基本路径
	assetsDir: 'static',
	publicPath: process.env.NODE_ENV === "production" ? "/" : "/",
	// 输出文件目录
	outputDir: 'my-app', // 默认dist
	// 用于嵌套生成的静态资产（js,css,img,fonts）目录
	// assetsDir: '',
	// 指定生成的 index.html 的输出路径 (相对于 outputDir)。也可以是一个绝对路径
	indexPath: 'index.html', // Default: 'index.html'
	filenameHashing: true,
	// 构建多页时使用
	pages: undefined,
	// eslint-loader是否在保存的时候检查
	lintOnSave: true,
	// 是否使用包含运行时编译器的Vue核心的构建
	runtimeCompiler: false,
	// 默认情况下 babel-loader 会忽略所有 node_modules 中的文件。如果你想要通过 Babel 显式转译一个依赖，可以在这个选项中列出来
	transpileDependencies: [],
	// 如果你不需要生产环境的 source map，可以将其设置为 false 以加速生产环境构建。
	productionSourceMap: false,
	// 如果这个值是一个对象，则会通过 webpack-merge 合并到最终的配置中。如果这个值是一个函数，则会接收被解析的配置作为参数。该函数及可以修改配置并不返回任何东西，也可以返回一个被克隆或合并过的配置版本。


	// css相关配置
	css: {
		// 启用 CSS modules
		modules: false,
		// 是否使用css分离插件
		extract: true,
		// 开启 CSS source maps?
		sourceMap: false,
		// css预设器配置项
		loaderOptions: {},
	},

    devServer: {
			port: 80, // 端口号
			host: "0.0.0.0",
			// https: false,
			// open: true, //配置自动启动浏览器
			disableHostCheck: true,
    	}
    };
