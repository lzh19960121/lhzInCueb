import Vue from 'vue'
import Router from 'vue-router'
// 导入刚才编写的组件
import Login from '@/components/Login'
import Home from "@/components/Home";
import AppIndex from "@/components/home/AppIndex";
import Admin from "@/components/admin/Admin";
import TemplateCreateIndex from "../components/answer_template/TemplateCreateIndex";
import CreateCenter from "@/components/answer_template/CreateCenter";
import MyTemplate from "@/components/answer_template/MyTemplate";
import EditTemplate from "@/components/answer_template/EditTemplate";
import Market from "../components/market/Market";
import Rank from "../components/rank/Rank";
Vue.use(Router)

export default new Router({
    mode: 'history',
    routes: [
        {
            path: '/',
            name: 'Home',
            component: Home,
            // home页面并不需要被访问
            redirect: '/',
            children: [
                {
                    path: '/admin',
                    name: 'Admin',
                    component: Admin
                },
                {
                    path: '/',
                    name: 'AppIndex',
                    component: AppIndex,
                    meta: {
                        requireAuth: false
                    }
                }, {
                    path: '/market',
                    name: 'Market',
                    component: Market,
                    meta: {
                        requireAuth: false
                    }
                },
                {
                    path: '/rank',
                    name: 'Rank',
                    component: Rank,
                    meta: {
                        requireAuth: false
                    }
                },
                {
                    path: '/template',
                    name: 'TemplateCreateIndex',
                    component: TemplateCreateIndex,
                    meta: {
                        requireAuth: true
                    },
                    children: [
                        {
                            path: '/add-template',
                            name: 'CreateCenter',
                            component: CreateCenter,
                            meta: {
                                requireAuth: true
                            },
                        },
                        {
                            path: '/my-template',
                            name: "MyTemplate",
                            component: MyTemplate,
                            meta: {
                                requireAuth: true
                            }
                        },
                        {
                            path: '/edit-template',
                            name: "EditTemplate",
                            component: EditTemplate,
                            meta: {
                                requireAuth: true
                            }
                        }
                    ]

                }
            ]
        },
        {
            path: '/login',
            name: 'Login',
            component: Login
        },


        {
            path: '/',
            name: 'Home',
            component: Home,
            redirect: '/',
            meta: {
                requireAuth: true
            }

        }
    ]

})

