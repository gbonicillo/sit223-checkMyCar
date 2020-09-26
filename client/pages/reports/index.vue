<template>
    <general-contents-container page-title="Reports">
        <template v-slot:header-extra>
            <b-button
                v-if="$auth.user.is_staff"
                variant="primary"
                class="float-lg-right float-sm-left"
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
        <b-row align-h="center">
            <b-pagination
                v-model="curPage"
                :total-rows="contentCount"
                :per-page="perPage"
            />
        </b-row>
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
            perPage: process.env.paginationItemsPerPage,
            curPage: 1,
            reports: []
        };
    },
    watch: {
        curPage: {
            handler (value) {
                this.fetchPage();
            }
        }
    },
    methods: {
        onRowClick (record, index) {
            const reportId = this.reports[index].id;

            this.$router.push({
                path: `/reports/${reportId}`
            });
        },
        async fetchPage () {
            try {
                const result = await this.$axios.$get(`/api/reports/?page=${this.curPage}`);
                this.reports = result.results;
                this.nextPage = result.next;
                this.prevPage = result.previous;
            } catch (err) {
                this.$toasted.global.defaultError({
                    msg: err
                });
            }
        }
    }
};
</script>

<style lang="scss" scoped>
</style>
