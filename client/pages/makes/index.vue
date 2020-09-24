<template>
    <div>
        <b-row align-v="center">
            <b-col cols="8">
                <page-header page-title="Makes" />
            </b-col>
            <b-col cols="4">
                <b-button
                    v-if="$auth.user.is_staff"
                    variant="primary"
                    class="float-right"
                    to="/makes/add"
                >
                    Add Make
                </b-button>
            </b-col>
        </b-row>
        <b-table
            striped
            hover
            selectable
            responsive
            borderless
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
