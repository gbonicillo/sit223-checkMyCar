<template>
    <general-contents-container page-title="Owned Cars">
        <b-row>
            <b-table
                striped
                hover
                selectable
                responsive
                borderless
                :fields="fields"
                :items="cars"
                @row-clicked="onRowClick"
            />
        </b-row>
    </general-contents-container>
</template>

<script>
import GeneralContentsContainer from "@/components/GeneralContentsContainer";

export default {
    components: {
        GeneralContentsContainer
    },
    async asyncData ({ $axios, params, $auth }) {
        try {
            const result = await $axios.$get(`/api/users/${$auth.user.id}/owned-cars`);
            return {
                cars: result.results,
                contentCount: result.count,
                nextPage: result.next,
                prevPage: result.previous
            };
        } catch (err) {
            return { cars: [] };
        }
    },
    middleware: "auth",
    data () {
        return {
            fields: [
                {
                    key: "model",
                    sortable: true
                },
                {
                    key: "make",
                    sortable: true
                }
            ],
            cars: []
        };
    },
    methods: {
        onRowClick (record, index) {
            const carId = this.cars[index].id;

            this.$router.push({
                path: `/cars/${carId}`
            });
        }
    }
};
</script>

<style lang="scss" scoped>
</style>
