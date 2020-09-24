<template>
    <div>
        <page-header :page-title="this.$auth.user.username" />

        <h2>Details</h2>
        <p>
            <b>Name:</b> {{ this.$auth.user.first_name + " " + this.$auth.user.last_name }}
            <br>
            <b>Email:</b> {{ this.$auth.user.email }}
        </p>
    </div>
</template>

<script>
import PageHeader from "@/components/PageHeader";

export default {
    components: {
        PageHeader
    }
};
</script>

<style lang="scss" scoped>

</style>
