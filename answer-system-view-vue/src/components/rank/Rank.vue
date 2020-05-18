<template>
    <el-container style="width:85%;alignment: center;margin: auto;">
        <el-header style="margin-top: 1%">
            <el-button @click="drawer = true" type="primary" style="margin-left: 16px;">
                参数设置
            </el-button>

            <el-drawer

                    :visible.sync="drawer"
                    :direction="direction"
            >

                <el-form v-model="filter_index" style="text-align: left;margin: 5%">
                    <el-card class="box-card">
                        <div slot="header" class="clearfix">
                            <span>设定参数</span>
                        </div>
                        <div class="text item">
                            <el-form-item label="涨跌区间(%)：">
                                <el-input v-model="filter_index.raise_fall_zone_fall" style="width: 50px"
                                          placeholder="-1"></el-input>

                                <i class="el-icon-arrow-left"></i>

                                <span>  涨跌  </span>
                                <i class="el-icon-arrow-left"></i>
                                <el-input v-model="filter_index.raise_fall_zone_rise" style="width: 50px"
                                          placeholder="2"></el-input>

                            </el-form-item>
                            <el-form-item label="价差(%)：">
                                <span>  大于 </span>
                                <el-input v-model="filter_index.gap_price" style="width: 50px"
                                          placeholder="2"></el-input>

                            </el-form-item>


                            <el-form-item label="瞬涨(%): ">
                                <span>  大于 </span>
                                <el-input v-model="filter_index.instant_rise" style="width: 50px"
                                          placeholder="1"></el-input>
                            </el-form-item>

                            <el-form-item label="瞬跌(%)：">
                                <span>  小于 </span>
                                <el-input v-model="filter_index.instant_fall" style="width: 50px"
                                          placeholder="-2"></el-input>
                            </el-form-item>

                            <el-form-item label="分钟数：">
                                <el-input v-model="filter_index.how_many_minute" style="width: 50px"
                                          placeholder="1"></el-input>
                            </el-form-item>
                            <el-form-item label="分钟涨(%)：">
                                <span>  大于 </span>
                                <el-input v-model="filter_index.minute_rise" style="width: 50px"
                                          placeholder="1"></el-input>
                            </el-form-item>
                            <el-form-item label="分钟跌(%)：">
                                <span>  小于 </span>
                                <el-input v-model="filter_index.minute_fall" style="width: 50px"
                                          placeholder="-2"></el-input>
                            </el-form-item>
                        </div>
                    </el-card>
                </el-form>
            </el-drawer>
        </el-header>


        <el-main>
            <el-table
                    :data="tableData"
                    :cell-style="tableCellClassName"
                    :default-sort = "{prop: 'filter_value', order: 'descending'}"
            >
                <el-table-column
                        prop="time"
                        label="时间"
                        width="200"
                >
                </el-table-column>
                <el-table-column
                        prop="stock"
                        label="股票"

                >
                </el-table-column>
                <el-table-column
                        prop="name"
                        label="名称"

                >
                </el-table-column>
                <el-table-column
                        prop="price"
                        label="价格(元)"
                >
                </el-table-column>
                <el-table-column
                        prop="volume"
                        label="数量"
                >
                </el-table-column>
                <el-table-column
                        prop="rise_fall"
                        label="涨跌(%)"
                >
                </el-table-column>
                <el-table-column
                        prop="filter_event"
                        label="事件"
                ></el-table-column>
                <el-table-column
                        prop="filter_value"
                        label="值"
                        sortable
                >
                </el-table-column>
            </el-table>
        </el-main>
    </el-container>
</template>


<style>

</style>
<script>
    export default {
        name: 'HelloWorld',
        data() {
            return {
                tableData: [],
                drawer: false,
                direction: 'rtl',
                filter_index: {
                    gap_price: 2,
                    instant_rise: 1,
                    instant_fall: -2,
                    minute_rise: 1,
                    minute_fall: -2,
                    raise_fall_zone_rise: 2,
                    raise_fall_zone_fall: -1,
                    how_many_minute: '1',
                },

            }
        },
        // html加载完成后执行initWebSocket()进行websocket初始化
        mounted() {
            this.initWebSocket()
        },
        // 离开该层时执行，划重点了！！！
        destroyed: function () {
            // 离开路由之后断开websocket连接
            this.websock.close()
        },
        methods: {
            start_filter() {
                this.initWebSocket()
            },

            tableCellClassName(row, column, rowIndex, columnIndex) {

                if (row.row.filter_event.indexOf('涨') !== -1) {
                    return 'color:red';
                }
                if (row.row.filter_event.indexOf('跌') !== -1) {
                    return 'color:green';
                }
            },

            // 初始化websocket
            initWebSocket() {
                const path = 'ws://47.105.39.71:8444'// 后台给的websocket的ip地址
                this.websock = new WebSocket(path)
                this.websock.onmessage = this.websocketOnMessage
                this.websock.onopen = this.websocketOnOpen
                this.websock.onerror = this.websocketOnError
                this.websock.onclose = this.websocketClose
            },
            // 连接建立成功的信号
            websocketOnOpen() {
                console.log('初始化成功')// 连接成功后就可以在这里写一些回调函数了
            },
            // 连接建立失败重连
            websocketOnError() {
                // 如果报错的话，在这里就可以重新初始化websocket，这就是断线重连
                this.initWebSocket()
            },
            // 数据接收
            websocketOnMessage(e) {

                // e这个变量就是后台传回的数据，在这个函数里面可以进行处理传回的值
                var basic_info_array = e.data.split('^');
                console.log(basic_info_array)
                var current_price = basic_info_array[4];
                var current_event = basic_info_array[7];
                var current_value = basic_info_array[8];
                var current_rise_fall_str = basic_info_array[6];
                var current_rise_fall = parseFloat(current_rise_fall_str);

                if (parseFloat(current_price) < 2) {
                    return;
                }
                if (current_rise_fall > this.filter_index.raise_fall_zone_rise || current_rise_fall < this.filter_index.raise_fall_zone_fall) {
                    return
                }

                if (current_event.indexOf(this.filter_index.how_many_minute + "分钟") === -1) {
                    return
                }

                if (current_event.indexOf("分钟涨") !== -1) {
                    var minute_rise = parseFloat(current_value)
                    if (minute_rise < this.filter_index.minute_rise) {
                        return
                    }
                }
                if (current_event.indexOf("分钟跌") !== -1) {
                    var minute_fall = parseFloat(current_value)
                    if (minute_fall > this.filter_index.minute_fall) {
                        return
                    }
                }
                if (current_event.indexOf("价差") !== -1) {
                    var gap_price = parseFloat(current_value);

                    if (gap_price < this.filter_index.gap_price) {
                        return
                    }
                }

                if (current_event.indexOf("瞬涨") !== -1) {
                    var instant_rise = parseFloat(current_value)
                    if (instant_rise < this.filter_index.instant_rise) {
                        return
                    }
                }
                if (current_event.indexOf("瞬跌") !== -1) {
                    var instant_fall = parseFloat(current_value)
                    if (instant_fall > this.filter_index.instant_fall) {
                        return
                    }
                }

                for (let x in this.tableData){
                    if (this.tableData[x].stock === basic_info_array[3]){
                        if(this.tableData[x].filter_value <= parseFloat(current_value)){
                          delete this.tableData[x];
                          break;
                        }else {
                            return;
                        }
                    }
                }
                this.tableData.unshift({
                    "time": basic_info_array[0] + " " + basic_info_array[1],
                    "name": basic_info_array[2],
                    "stock": basic_info_array[3],
                    "price": basic_info_array[4],
                    "volume": basic_info_array[5],
                    "rise_fall": basic_info_array[6] + "%",
                    "filter_event": current_event,
                    "filter_value":  parseFloat(current_value)
                })// 这边我绑定了一个data，data会在网页上显示后端传来的东西


            },
            // 数据发送
            websocketSend(Data) {
                this.websock.send(Data)// Data变量就是你想对后台说些啥，根据后端给你的接口文档传值进行交互
            },
            // 关闭的信号
            websocketClose() {
                console.log('断开连接')
            },
            // 传参给后端，这里对websocketSend又进行了一层封装，用不到的可以删除
            sendDevName(chooseDevice) {
                console.log(chooseDevice)
                this.websocketSend(chooseDevice)
            }
        }
    }
</script>

