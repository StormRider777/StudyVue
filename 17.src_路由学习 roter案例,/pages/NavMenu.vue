<template>
    <div>
        <ul>
            <li><router-link to="/about">关于</router-link></li>
            <li><router-link to="/work">业务</router-link></li>
            <li><router-link to="/test">随机</router-link></li>
        </ul>
    </div>
</template>

<script>
    export default {
        name: "NavMenu"
    }
</script>

<style scoped>
    ul {
        list-style-type: none;
        padding: 0;
        width: 100%;
    }

    li {
        height: 40px;
        font-size: 18px;
        display: block;
        width: 100%;
        line-height: 40px;
        padding-left: 10px;
    }

    li:hover {
        background: skyblue;
        color: red;
    }

    a {
        text-decoration: none;
        color: white;
    }

    a:visited {
        color: white;
    }

    a:hover {
        color: red;
    }
</style>