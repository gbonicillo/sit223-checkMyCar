<template>
    <general-contents-container :page-title="car.make + ' ' + car.model">
        <template v-slot:header-extra>
            <add-delete-buttons
                :update-to="`/cars/${car.id}/update`"
                :delete-function="onDeleteClick"
            />
        </template>
        <h2>Reports</h2>
        <b-table
            v-if="car.reports.length > 0"
            striped
            hover
            selectable
            responsive
            borderless
            :fields="report_fields"
            :items="car.reports"
            @row-clicked="onRowClick"
        />
        <h2
            v-else
            class="text-muted"
        >
            <em>There are no reports on this car yet</em>
        </h2>
    </general-contents-container>
</template>

<script>
import GeneralContentsContainer from "@/components/GeneralContentsContainer";
import AddDeleteButtons from "@/components/AddDeleteButtons";

export default {
    components: {
        GeneralContentsContainer,
        AddDeleteButtons
    },
    async asyncData ({ $axios, params, error }) {
        try {
            const car = await $axios.$get(`/api/cars/${params.id}`);
            return {
                car
            };
        } catch (err) {
            error({ statusCode: 404, message: "Car not found" });
        }
    },
    data () {
        return {
            car: {
                id: 0,
                make: "",
                model: "",
                reports: []

            },
            report_fields: [
                {
                    key: "type",
                    sortable: true
                },
                {
                    key: "title",
                    sortable: true
                },
                {
                    key: "created_at",
                    label: "Date Reported",
                    sortable: true
                },
                {
                    key: "updated_at",
                    label: "Last Updated",
                    sortable: true
                }
            ]
        };
    },
    methods: {
        onRowClick (record, index) {
            const reportId = this.car.reports[index].id;

            this.$router.push({
                path: `/reports/${reportId}`
            });
        },
        async onDeleteClick (evt) {
            const carName = this.car.make + " " + this.car.model;
            const result = confirm(`Are you sure you want to delete ${carName}`);
            if (result) {
                await this.$axios.delete(`/api/cars/${this.car.id}`)
                    .then((response) => {
                        this.$router.push({
                            path: "/cars/"
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
