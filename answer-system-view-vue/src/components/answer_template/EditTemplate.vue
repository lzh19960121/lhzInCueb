<template>
    <el-card>
          <el-page-header @back="goBack" content="b">
                </el-page-header>
        <div slot="header">
            <el-popover
                    placement="right"
                    trigger="click"
                    width="50%">
                <div class="block">
                    <span class="demonstration">选择模板类型</span>
                    <span class="demonstration">：</span>
                    <el-cascader
                            :options="options"
                            filterable
                            placeholder="试试搜索：指南">
                    </el-cascader>
                    <el-button style="float: right">确定</el-button>
                </div>
                <el-button class="el-icon-document-add" slot="reference" style="float: left;padding: 3px 0"
                           type="text"></el-button>
            </el-popover>

            <span>写作台</span>
            <el-button style="float: right; padding: 3px 0" type="text">清空</el-button>
            <el-button style="float: right; padding: 3px 0" type="text"></el-button>
            <el-button style="float: right; padding: 3px 0" type="text">保存</el-button>
        </div>
        <el-divider>
            类型： 子类型： 标题：
        </el-divider>
        <div class="text" contenteditable="true" style="min-height: 400px ;text-align: left">
            <div :key="o" class="text item" style="display: inline;" v-for="o in 4">
                <el-button type="text" style="display: inline" v-if="o===1"> {{o}}</el-button>
                <p style="display: inline" v-else> {{o}} </p>
            </div>
        </div>

    </el-card>
</template>

<script>
    export default {
        name: "EditTemplate"
    }
</script>

<style scoped>

</style>
