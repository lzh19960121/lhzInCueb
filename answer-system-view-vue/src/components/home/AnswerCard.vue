<template>
    <el-card class="box-card">
        <div slot="header">
            <span style="font-weight: bold;font-size: 15px">智能问答系统</span>
            <!--<el-button style="float: right; padding: 3px 0" type="text">修改</el-button>-->
        </div>

        <div id="dia_container">
            <div v-for=" (v,k) in text_dialog">
                <el-divider content-position="left">{{user_name.username}} --{{v.time}}</el-divider>
                <span id="question_card" style="font-size: 15px">{{v.question}}</span>
                <el-divider content-position="right">回答</el-divider>
                <span id="answer_card"><div style="font-size: 15px" v-html="v.answer"></div></span>
            </div>
        </div>
        <el-divider content-position="right"></el-divider>
        <el-input
                type="textarea"
                :autosize="{ minRows: 2, maxRows: 4}"
                placeholder="尝试输入，上市公司名称，如：格力空调\海澜之家最近上涨吗？平安银行估值怎么样？"
                v-model="txt_question"
        >
        </el-input>
        <el-divider content-position="right">
            <el-button @click="ask_question()">提问</el-button>
        </el-divider>
    </el-card>


</template>

<script>
    import qs from 'qs'
    import NavMenu from "../common/NavMenu";
    export default {
        name: 'UpdateCard',
        mounted() {
            this.scrollToBottom();
        },
        //每次页面渲染完之后滚动条在最底部
        updated: function () {
            this.scrollToBottom();
        },
        watch: {
            'processData': 'scrollToBottom'
        },

        methods: {
            scrollToBottom: function () {
                this.$nextTick(() => {
                    const div = document.getElementById('dia_container')
                    div.scrollTop = div.scrollHeight
                })

            },
            ask_question() {
                if (this.txt_question === '') {
                    alert("输入不能为空")
                    return
                }
                this.text_question = this.txt_question
                console.log(this.txt_question)
                this.$axios.post('http://47.105.39.71:8445/question_controller/', qs.stringify({
                    txt_question: this.txt_question
                })).then(successResponse => {
                    console.log(successResponse.data.data)
                    // 添加一条 问答对话
                    var myDate = new Date();
                    this.text_dialog.push({time:myDate.toLocaleString(), question: this.txt_question, answer: successResponse.data.data})
                }).catch(failResponse => {
                    alert(failResponse)
                })

            }
        },
        data() {
            return {
                user_name:NavMenu.data().username,
                txt_question: '',
                text_question: '',
                text_dialog: [],
            }
        }
    }
</script>

<style scoped>
    #dia_container {
        overflow: auto;
        scroll-margin-right: 1px;
        min-height: calc(100vh - 360px);
        max-height: calc(100vh - 360px) ;
    }

    .box-card {
        min-height: calc(100vh - 120px);
        max-height: calc(100vh - 120px);
        margin: auto;
        width: 50%;
        min-width: 900px;
        text-align: left;
    }

</style>
