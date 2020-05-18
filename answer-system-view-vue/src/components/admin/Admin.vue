<template>
    <el-container style="width:85%;alignment: center;margin: auto;">
        <el-header >

        </el-header>

        <el-main>
            <el-row :gutter="20">
                <el-col :span="6">
                        <el-card class="box-card">
                            <div slot="header" class="clearfix">
                                <span>过滤器状态</span>
                                <el-button style="float: right; padding: 3px 0" icon="el-icon-switch-button" type="text">开启</el-button>
                            </div>
                            <div class="text item">
                            </div>
                        </el-card>
                </el-col>
                <el-col :span="6">
                    <div class="grid-content bg-purple"></div>
                </el-col>
                <el-col :span="6">
                    <div class="grid-content bg-purple"></div>
                </el-col>
                <el-col :span="6">
                    <div class="grid-content bg-purple"></div>
                </el-col>
            </el-row>
        </el-main>
    </el-container>


</template>

<script>
    // window.location.href = 'http://47.105.39.71:8445/admin'
    export default {
        name: "Admin"
    }
</script>

<style scoped>

</style>
