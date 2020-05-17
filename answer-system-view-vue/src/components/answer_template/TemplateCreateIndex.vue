<template>
    <el-container>
        <el-container>
            <!--左侧导航栏-->
            <el-aside width="10%">
                <LeftMenu></LeftMenu>
            </el-aside>
            <!--中间部分-->
            <el-main>
                <router-view/>
            </el-main>
        </el-container>
    </el-container>

</template>

<script>
    import LeftMenu from "@/components/answer_template/LeftMenu";

    export default {
        name: "TemplateCreateIndex",
        components: {LeftMenu},
        methods:{
            loadBooks () {
                var _this = this
                this.$axios.get('/search').then(resp => {
                    if (resp && resp.data.code === 200) {
                        _this.books = resp.data.result
                    }
                })
            }
        },

        data() {
            const item = {
                date: '2016-05-02',
                name: '王小虎',
                address: '上海市普陀区金沙江路 1518 弄'
            };
            return {
                tableData: Array(20).fill(item)
            }
        }
    }
</script>
<style>



</style>

