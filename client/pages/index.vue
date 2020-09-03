<template>
    <b-container>
        <b-row>
            <b-card
                v-for="car in cars"
                :key="car.id"
                :title="car.make + ' ' + car.model"
                class="col-lg-4 col-md-6 mb-3 mt-3"
            />
        </b-row>
    </b-container>
</template>

<script>
export default {
    async asyncData ({ $axios, params }) {
        try {
            const cars = await $axios.$get("/cars/");
            return {
                cars
            };
        } catch (err) {
            return { cars: [] };
        }
    },
    data () {
        return {
            cars: []
        };
    }
};
</script>

<style lang="scss" scoped>

</style>
