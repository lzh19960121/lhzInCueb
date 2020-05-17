<template>
    <el-card class="create-center">
        <div slot="header">
            <span>写作台</span>
            <el-button style="float: right; padding: 3px 0" type="text">清空</el-button>
            <el-button style="float: right; padding: 3px 0" type="text"></el-button>
            <el-button style="float: right; padding: 3px 0" type="text">保存</el-button>
        </div>
        <el-divider>
            <div style="float: left" class="block">
                <span class="demonstration">选择模板类型</span>
                <span class="demonstration">：</span>
                <el-cascader
                        :options="options"
                        filterable
                        placeholder="试试搜索股票">
                </el-cascader>
            </div>
        </el-divider>

        <div class="text" contenteditable="true" style=" ;text-align: left">
            <div :key="o" class="text item" style="display: inline;" v-for="o in 4">
                <el-button type="text" style="display: inline" v-if="o===1"> {{o}}</el-button>
                <p style="display: inline" v-else> {{o}} </p>
            </div>
        </div>
    </el-card>

</template>

<script>

    export default {
        name: "CreateCenter",
        components: {},
        data() {
            return {
                options: [{
                    value: 'zhinan',
                    label: '股票',
                    children: [{
                        value: 'shejiyuanze',
                        label: '股票',
                        children: [{
                            value: 'yizhi',
                            label: '股票'
                        },]
                    }]
                }, {
                    value: 'zujian',
                    label: '外盘',
                    children: [{
                        value: 'basic',
                        label: '贵金属',
                        children: [{
                            value: 'layout',
                            label: 'Layout 布局'
                        }]
                    }, {
                        value: 'form',
                        label: '大宗商品',
                        children: [{
                            value: 'radio',
                            label: 'Radio 单选框'
                        }]
                    }, {
                        value: 'data',
                        label: '美元',
                        children: [{
                            value: 'table',
                            label: 'Table 表格'
                        }]
                    }, {
                        value: 'notice',
                        label: '美债',
                        children: [{
                            value: 'alert',
                            label: 'Alert 警告'
                        },]
                    }, {
                        value: 'navigation',
                        label: '美股',
                        children: [{
                            value: 'menu',
                            label: 'NavMenu 导航菜单'
                        },]
                    }, {
                        value: 'others',
                        label: '利率',
                        children: [{
                            value: 'dialog',
                            label: 'Dialog 对话框'
                        }]
                    }]
                }, {
                    value: 'ziyuan',
                    label: '保险',
                    children: [{
                        value: 'axure',
                        label: '理财险'
                    }, {
                        value: 'sketch',
                        label: '保障险'
                    }, {
                        value: 'jiaohu',
                        label: '财产险'
                    }]
                }, {
                    value: 'shuiwu',
                    label: '税务',
                    children: [{
                        value: 'shuiwuhege',
                        label: '税务合格'
                    }, {
                        value: 'shuiwuchouhua',
                        label: '税务筹划'
                    }, {
                        value: 'shuiwupuji',
                        label: '税务普及知识'
                    }, {
                        value: 'anli',
                        label: '案例'
                    }]
                }]
            };
        }
    }
</script>

<style scoped>
    .create-center{
        width: 70%;
        min-height: 600px;
        height: 100%;
    }
</style>
