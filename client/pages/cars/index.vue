<template>
    <div>
        <page-header page-title="Cars" />
        <b-table
            striped
            hover
            selectable
            :fields="fields"
            :items="cars"
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
