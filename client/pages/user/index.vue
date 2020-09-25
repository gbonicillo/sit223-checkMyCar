<template>
    <general-contents-container :page-title="this.$auth.user.username">
        <h2>Details</h2>
        <p>
            <b>Name:</b> {{ this.$auth.user.first_name + " " + this.$auth.user.last_name }}
            <br>
            <b>Email:</b> {{ this.$auth.user.email }}
        </p>
    </general-contents-container>
</template>

<script>
import GeneralContentsContainer from "@/components/GeneralContentsContainer";

export default {
    middleware: "auth",
    components: {
        GeneralContentsContainer
    }
};
</script>

<style lang="scss" scoped>

</style>
