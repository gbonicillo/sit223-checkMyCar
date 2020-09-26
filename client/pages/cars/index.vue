<template>
    <general-contents-container page-title="Cars">
        <template v-slot:header-extra>
            <b-button
                v-if="$auth.user.is_staff"
                variant="primary"
                class="float-right"
                to="/cars/add"
            >
                Add Car
            </b-button>
        </template>
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
    async asyncData ({ $axios, params }) {
        try {
            const result = await $axios.$get("/api/cars/");
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
