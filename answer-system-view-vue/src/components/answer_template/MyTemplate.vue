<template>
    <!--    <el-card id="my-template">-->
    <!--        <div slot="header">-->
    <!--            <span>我的写作</span>-->
    <!--            <el-button style="float: right; padding: 3px 0" type="text">清空</el-button>-->
    <!--            <el-button style="float: right; padding: 3px 0" type="text"></el-button>-->
    <!--            <el-button style="float: right; padding: 3px 0" type="text">保存</el-button>-->
    <!--        </div>-->
    <el-container class="template-table-container">
        <el-header>
            <el-autocomplete
                    popper-class="my-autocomplete"
                    v-model="state"
                    :fetch-suggestions="querySearch"
                    placeholder="请输入内容"
                    @select="handleSelect"
            style="float: left"
            >
                <i class="el-icon-edit el-input__icon" slot="suffix" @click="handleIconClick"> </i>
                <template slot-scope="{ item }">
                    <div class="name">{{ item.value }}</div>
                    <span class="addr">{{ item.address }}</span>
                </template>
            </el-autocomplete>

        </el-header>
        <el-main>
            <el-table  height="100%" :data="template_data.slice((currentPage-1)*pagesize,currentPage*pagesize)"
                      class="answer-template-table">
                <el-table-column
                        label="日期"
                        width="180">
                    <template slot-scope="scope">
                        <i class="el-icon-time"></i>
                        <span style="margin-left: 10px">{{ scope.row.date }}</span>
                    </template>
                </el-table-column>
                <el-table-column
                        label="姓名"
                        width="180">
                    <template slot-scope="scope">
                        <el-popover trigger="hover" placement="top">
                            <p>姓名: {{ scope.row.name }}</p>
                            <p>住址: {{ scope.row.address }}</p>
                            <div slot="reference" class="name-wrapper">
                                <el-tag size="medium">{{ scope.row.name }}</el-tag>
                            </div>
                        </el-popover>
                    </template>
                </el-table-column>
                <el-table-column label="操作">
                    <template slot-scope="scope">
                        <el-button
                                size="mini"
                                @click="handleEdit(scope.$index, scope.row)">编辑
                        </el-button>
                        <el-button
                                size="mini"
                                type="danger"
                                @click="handleDelete(scope.$index, scope.row)">删除
                        </el-button>
                    </template>
                </el-table-column>
            </el-table>
        </el-main>
        <el-footer>
            <el-pagination
                    background
                    :page-sizes="[5, 10, 20, 40]"
                    :page-size="pagesize"
                    @size-change="handleSizeChange"
                    :total="blogList.length"
                    @current-change="handleCurrentChange"
                    layout="prev, pager, next">
            </el-pagination>

        </el-footer>


    </el-container>
    <!--    </el-card>-->
</template>

<script>
    function load_current_author_template() {

    }


    export default {
        name: "MyTemplate",

        data() {
            const item = {
                date: '2016-05-02',
                name: '王小虎',
                address: '上海市普陀区金沙江路asddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd 1518 弄'
            };
            return {
                input: '',
                currentPage:1,
                pagesize:10,
                searchInfo: '',
                templateList: [],
                template_data: Array(10).fill(item),
                tableData: Array(10).fill(item)
            }
        },
        mounted: function () {
            this.showBlogs()
        },
        methods: {
            handleEdit(index, row) {
                console.log(index, row);
            },
            handleDelete(index, row) {
                console.log(index, row);
            },
            handleCurrentChange: function(currentPage){
                this.currentPage = currentPage;
                console.log(this.currentPage)  //点击第几页
            },
            handleSizeChange: function (size) {
                this.pagesize = size;
                console.log(this.pagesize)  //每页下拉显示数据
            },

            showBlogs () {
                this.$axios.get('/get_template_by_author/')
                    .then((response) => {
                        var res = JSON.parse(response);
                        console.log(res.list.length);
                        if (res.code === 0) {
                            this.blogList = res['list']
                        }
                    })
            }
        }
    }
</script>

<style scoped>



</style>
