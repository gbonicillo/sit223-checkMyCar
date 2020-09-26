<template>
    <b-container>
        <b-row>
            <div
                v-for="car in cars"
                :key="car.id"
                class="col-lg-4 col-md-6 mb-3 mt-3"
            >
                <b-card
                    :title="car.make + ' ' + car.model"
                />
            </div>
        </b-row>
    </b-container>
</template>

<script>
export default {
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
            cars: []
        };
    }
};
</script>

<style lang="scss" scoped>

</style>
