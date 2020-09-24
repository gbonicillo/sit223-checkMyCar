<template>
    <div id="main-container">
        <navbar />
        <b-container id="contents" class="p-1 h-100">
            <Nuxt />
        </b-container>
    </div>
</template>

<script>
import Navbar from "../components/Navbar";

export default {
    components: {
        Navbar
    }
};
</script>

<style lang="scss">

@import '@/assets/theme-colors.scss';
@import '@/node_modules/bootstrap/scss/bootstrap';
@import '@/node_modules/bootstrap-vue/src/index.scss';

html{
    height: 100%;
}

body {
    // background-color: ;
    min-height: 100%
}

#main-container {
    min-height: 100%
}

// #contents {
//     background-color: #f9f5d7;
//     padding: 20px 20px;
//     min-height: 100%
// }

#__nuxt, #__layout{
    height: 100%;
    min-height: 100%
}

.dropdown-item:hover, .dropdown-item:focus {
    text-decoration: none;
    background-color: #f2e5bc;
}
</style>
