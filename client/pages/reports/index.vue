<template>
    <div>
        <b-row align-v="center">
            <b-col cols="8">
                <page-header page-title="Reports" />
            </b-col>
            <b-col cols="4">
                <b-button
                    v-if="$auth.user.is_staff"
                    variant="primary"
                    class="float-right"
                    to="/reports/add"
                >
                    Add Report
                </b-button>
            </b-col>
        </b-row>
        <b-table
            striped
            hover
            selectable
            responsive
            :fields="fields"
            :items="reports"
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
            const reports = await $axios.$get("/api/reports/");
            return {
                reports
            };
        } catch (err) {
            return { reports: [] };
        }
    },
    data () {
        return {
            fields: [
                {
                    key: "car",
                    sortable: true
                },
                {
                    key: "title",
                    sortable: true
                },
                {
                    key: "created_at",
                    sortable: true,
                    label: "Created"
                },
                {
                    key: "updated_at",
                    sortable: true,
                    label: "Last Updated"
                }
            ],
            reports: []
        };
    },
    methods: {
        onRowClick (record, index) {
            const reportId = this.reports[index].id;

            this.$router.push({
                path: `/reports/${reportId}`
            });
        }
    }
};
</script>

<style lang="scss" scoped>
</style>
