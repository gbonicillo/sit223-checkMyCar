<template>
    <general-contents-container :page-title="make.name">
        <h2>Models</h2>
        <b-table
            striped
            hover
            selectable
            :fields="fields"
            :items="make.cars"
            @row-clicked="onRowClick"
        />
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
            const make = await $axios.$get(`/api/makes/${params.id}`);
            return {
                make
            };
        } catch (err) {
            return {
                make: {
                    id: 0,
                    name: "",
                    cars: []
                }
            };
        }
    },
    data () {
        return {
            fields: ["model"],
            make: {
                id: 0,
                name: "",
                cars: []
            }
        };
    },
    methods: {
        onRowClick (record, index) {
            const carId = this.make.cars[index].id;

            this.$router.push({
                path: `/cars/${carId}`
            });
        }
    }
};
</script>

<style lang="scss" scoped>

</style>
