<template>
    <el-row>
        <el-col background-color="#252525">
            <el-menu :default-active="'/index'"
                     router
                     mode="horizontal"
                     background-color="#252525"
                     text-color="#fff"
                     active-text-color="#ffd04b"
                     style="min-width:1300px;align-content: center;">
                <!--                     background-color="black"-->
                <!--                     text-color="white"-->
                <!--                     active-text-color="red"-->
                <el-menu-item v-for="(item,i) in navList" :key="i" :index="item.name">
                    {{ item.navItem }}
                </el-menu-item>

                 <span style="position: absolute;color:#fff ;padding-top: 20px;right: 43%;font-size: 20px;font-weight: bold">Securities industry Q & A</span>

                <el-menu-item style="float: right" @click="logout()">
                    登出
                </el-menu-item>

                <el-menu-item style="float: right" :index="'/personal'">
                    用户：{{username.username}}
                </el-menu-item>

                <el-menu-item :index="'/admin'" style="float: right;">
                    <a  style="font-size: 35px;" class="el-icon-menu" ></a>
                </el-menu-item>
            </el-menu>
        </el-col>
    </el-row>

</template>

<script>
    var loginUsername = JSON.parse(window.localStorage.getItem('user' || '[]'))
    if (null == loginUsername) {
        loginUsername = {
            username: '游客'
        }
    }
    export default {
        name: 'NavMenu',
        methods: {
            logout() {

            },
        },
        data() {
            return {
                username: {
                    username: loginUsername.username
                },
                navList: [
                    {name: '/', navItem: '首页'},
                    {name: '/document', navItem: '帮助文档'},
                    {name: '/template', navItem: '创作模板'},
                    {name: '/market', navItem: '行情监控'},
                    {name: '/rank', navItem: '排行'},
                ]
            }
        }
    }
</script>

<style scoped>
    a {
        text-decoration: none;
    }

    span {
        pointer-events: none;
    }
</style>

