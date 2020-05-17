import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
Vue.config.productionTip = false
import ElementUI from 'element-ui'
import Vant from 'vant';
import 'element-ui/lib/theme-chalk/index.css'
import 'vant/lib/index.css';



var axios = require('axios')

Vue.prototype.$axios = axios
Vue.config.productionTip = false
Vue.use(Vant);
Vue.use(ElementUI)

router.beforeEach((to, from, next) => {
      if (to.meta.requireAuth) {
        if (store.state.user.username) {
          next()
        } else {
          next({
            path: 'login',
            query: {redirect: to.fullPath}
          })
        }
      } else {
        next()
      }
    }
)

new Vue({
  store,
  router,
  render: h => h(App),
}).$mount('#app')
