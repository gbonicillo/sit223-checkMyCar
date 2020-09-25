<template>
    <general-contents-container :page-title="make.name">
        <template v-slot:header-extra>
            <b-button
                v-if="$auth.user.is_staff"
                variant="primary"
                class="float-right"
                :to="`/makes/${make.id}/update`"
            >
                Update
            </b-button>
        </template>
        <h2>Models</h2>
        <b-table
            striped
            hover
            selectable
            borderless
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
    async asyncData ({ $axios, params, error }) {
        try {
            const make = await $axios.$get(`/api/makes/${params.id}`);
            return {
                make
            };
        } catch (err) {
            error({ statusCode: 404, message: "Make not found" });
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
