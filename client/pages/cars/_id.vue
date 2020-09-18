<template>
    <div>
        <page-header :page-title="car.make + ' ' + car.model" />
        <b-table
            v-if="car.reports.length > 0"
            striped
            hover
            selectable
            :items="car.reports"
            @row-clicked="onRowClick"
        />
        <h2
            v-else
        >
            There are no reports on this car yet
        </h2>
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
            const car = await $axios.$get(`/api/cars/${params.id}`);
            return {
                car
            };
        } catch (err) {
            return {
                car: {
                    id: 0,
                    make: "",
                    model: "",
                    reports: []
                }
            };
        }
    },
    data () {
        return {
            car: {
                id: 0,
                make: "",
                model: "",
                reports: []

            }
        };
    },
    methods: {
        onRowClick (record, index) {
            const carId = this.car.cars[index].id;

            this.$router.push({
                path: `/cars/${carId}`
            });
        }
    }
};
</script>

<style lang="scss" scoped>

</style>
