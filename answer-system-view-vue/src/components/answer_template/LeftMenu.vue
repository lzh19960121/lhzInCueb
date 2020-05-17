<template>
    <el-menu :default-active="'/add'"
             router
             background-color="white"
             text-color="#222"
             active-text-color="red"
             class="el-menu">
        <el-menu-item v-for="(item,i) in navList" :key="i" :index="item.name">
            {{ item.navItem }}
        </el-menu-item>

    </el-menu>

</template>

<script>

    export default {
        name: "LeftMenu",
        data() {
            return {
                navList: [
                    {name: '/add-template', navItem: '创建'},
                    {name: '/my-template', navItem: '我的'},
                ]
            }
        },
        methods:{

        },
    }
</script>

<style scoped>
    .el-menu{
        height: 600px;
        min-height: 600px;
        margin-top: 10%;
    }

</style>
