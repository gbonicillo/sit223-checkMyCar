<template>
    <general-contents-container page-title="Reports">
        <template v-slot:header-extra>
            <b-button
                v-if="$auth.user.is_staff"
                variant="primary"
                class="float-right"
                to="/reports/add"
            >
                Add Report
            </b-button>
        </template>
        <b-table
            striped
            hover
            selectable
            responsive
            borderless
            :fields="fields"
            :items="reports"
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
            const result = await $axios.$get("/api/reports/");
            return {
                reports: result.results,
                contentCount: result.count,
                nextPage: result.next,
                prevPage: result.previous
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
