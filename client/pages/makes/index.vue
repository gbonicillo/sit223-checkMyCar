<template>
    <div>
        <page-header page-title="Makes" />
        <b-table
            striped
            hover
            selectable
            :fields="fields"
            :items="makes"
            @row-clicked="onRowClick"
        />
    </div>
</template>

<script>
import PageHeader from "@/components/PageHeader";

export default {
    components: {
        PageHeader
    },
    async asyncData ({ $axios, params }) {
        try {
            const makes = await $axios.$get("/api/makes/");
            return {
                makes
            };
        } catch (err) {
            return { makes: [] };
        }
    },
    data () {
        return {
            fields: ["name"],
            makes: []
        };
    },
    methods: {
        onRowClick (record, index) {
            const makeId = this.makes[index].id;

            this.$router.push({
                path: `/makes/${makeId}`
            });
        }
    }
};
</script>

<style lang="scss" scoped>
</style>
