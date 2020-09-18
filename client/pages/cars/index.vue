<template>
    <div>
        <b-row align-v="center">
            <b-col col="8">
                <page-header page-title="Cars" />
            </b-col>
            <b-col col="4">
                <b-button
                    v-if="$auth.user.is_staff"
                    variant="primary"
                    class="float-right"
                    to="/cars/add"
                >
                    Add Car
                </b-button>
            </b-col>
        </b-row>
        <b-row>
            <b-table
                striped
                hover
                selectable
                :fields="fields"
                :items="cars"
                @row-clicked="onRowClick"
            />
        </b-row>
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
            const cars = await $axios.$get("/api/cars/");
            return {
                cars
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
