<template>
    <!--    <el-row>-->
    <!--        <el-col background-color="#252525">-->
    <!--            <el-menu-->
    <!--                     mode="horizontal"-->
    <!--                     background-color="#252525"-->
    <!--                     text-color="#fff"-->
    <!--                     active-text-color="#ffd04b"-->
    <!--                     style="min-width:1300px;align-content: center;">-->
    <!--                &lt;!&ndash;                     background-color="black"&ndash;&gt;-->
    <!--                &lt;!&ndash;                     text-color="white"&ndash;&gt;-->
    <!--                &lt;!&ndash;                     active-text-color="red"&ndash;&gt;-->

    <!--                <el-menu-item style="">-->
    <!--                    智能问答系统-->
    <!--                </el-menu-item>-->
    <!--            </el-menu>-->
    <!--        </el-col>-->
    <!--        <el-col background-color="#252525">-->
    <!--            <el-menu-->
    <!--                     mode="horizontal"-->
    <!--                     background-color="#252525"-->
    <!--                     text-color="#fff"-->
    <!--                     active-text-color="#ffd04b"-->
    <!--                     style="min-width:1300px;align-content: center;">-->
    <!--                &lt;!&ndash;                     background-color="black"&ndash;&gt;-->
    <!--                &lt;!&ndash;                     text-color="white"&ndash;&gt;-->
    <!--                &lt;!&ndash;                     active-text-color="red"&ndash;&gt;-->

    <!--                <el-menu-item style="">-->
    <!--                    智能问答系统-->
    <!--                </el-menu-item>-->
    <!--            </el-menu>-->
    <!--        </el-col>-->
    <!--    </el-row>el-row-->
    <div class="footer">
        <div style="border-top:1px #1F1F1F solid;">
            <p class="alt" style="color:#fff; line-height:0">&copy; 版权所有：LHZ &nbsp;
                <span>技术支持：</span>
                <a href="" target="_blank" style="color:#fff;">LHZ</a>
            </p>

            <p class="alt" style="color:#fff; line-height:0">联系人：LHZ &nbsp;
                <span> </span>
                <a href="" target="_blank" style="color:#fff;">772046613</a>
            </p>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Foot"
    }
</script>

<style scoped>
    .footer {
        background-color: #252525;
    }

    .footer .alt {
        overflow: hidden;
        padding: 20px 0;
        width: 1160px;
        margin: auto;
    }

    .footer .alt .foot {
        width: 138px;
        float: left;
    }

    .footer .alt .foot p {
        color: #FFF;
        line-height: 28px;
    }

    a {
        text-decoration: none;
    }

    .footer .alt .foot a {
        color: #999;
        display: block;
        line-height: 24px;
    }
</style>