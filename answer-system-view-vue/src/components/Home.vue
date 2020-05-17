<template>
  <div>
    <nav-menu class="nav-menu"></nav-menu>
    <router-view/>
  </div>
</template>
<script>

  import NavMenu from '@/components/common/NavMenu'
  export default {
    // eslint-disable-next-line vue/no-unused-components
    components: {NavMenu}
  }
</script>

<style>
  .nav-menu {
    /*margin-bottom: 40px;*/
    box-shadow: 0 2px 4px 0 rgba(0,0,0,.05);
  }

  html,body,#app,.el-container{
    /*background: url("../assets/index.jpg");*/
    background: #F2F2F3;
    /*设置内部填充为0，几个布局元素之间没有间距*/
    padding: 0px;
    /*外部间距也是如此设置*/
    margin: 0px;
    /*统一设置高度为100%*/
    height: 100%;
  }


</style>
