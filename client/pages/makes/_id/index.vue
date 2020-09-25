<template>
    <general-contents-container :page-title="make.name">
        <template v-slot:header-extra>
            <add-delete-buttons
                :update-to="`/makes/${make.id}/update`"
                :delete-function="onDeleteClick"
            />
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
        },
        async onDeleteClick (evt) {
            const result = confirm(`Are you sure you want to delete ${this.make.name}`);
            if (result) {
                await this.$axios.delete(`/api/makes/${this.make.id}`)
                    .then((response) => {
                        this.$router.push({
                            path: "/makes/"
                        });
                    })
                    .catch((err) => {
                        this.$toasted.global.defaultError({
                            msg: err
                        });
                    });
            }
        }
    }
};
</script>

<style lang="scss" scoped>

</style>
