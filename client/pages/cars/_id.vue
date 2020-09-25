<template>
    <general-contents-container :page-title="car.make + ' ' + car.model">
        <h2>Reports</h2>
        <b-table
            v-if="car.reports.length > 0"
            striped
            hover
            selectable
            responsive
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

export default {
    components: {
        GeneralContentsContainer
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
        }
    }
};
</script>

<style lang="scss" scoped>

</style>
