<template>


    <el-container style="height: 100%">
        <el-main>
            <AnswerCard id="update-card">AnswerCard</AnswerCard>
        </el-main>
        <el-footer>
            <Foot id="index-foot"></Foot>
        </el-footer>
    </el-container>

    <!--    <div class="index-back">-->
    <!--        <el-row>-->
    <!--            <el-col style="padding-top: 2%">-->

    <!--            </el-col>-->
    <!--        </el-row>-->
    <!--    </div>-->
</template>

<script>
    import AnswerCard from './AnswerCard'
    import Foot from "../common/Foot";

    export default {
        name: 'AppIndex',
        components: {AnswerCard, Foot}
    }

    const user = document.cookie
    console.log(user)


</script>

<style scoped>
    /*.el-main {*/
    /*    min-height: calc(100vh - 120px)*/
    /*}*/
    .el-footer{
        padding: 0px;
    /*外部间距也是如此设置*/
        margin: 0px;
    }
    .index-back {
        width: 100%;
        margin: auto;
        background-size: cover;
    }


</style>
