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
            v-if="reports.length > 0"
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
    watchQuery: ["search"],
    async asyncData ({ $axios, params, route }) {
        try {
            let search = route.query.search || "";
            search = search.length > 0 ? `?search=${search}` : "";
            const result = await $axios.$get(`/api/reports/${search}`);
            return {
                search,
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
    created () {
        this.fetchPage();
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
                const params = this.search.length > 0 ? `${this.search}&` : "?";
                const result = await this.$axios.$get(`/api/reports/${params}page=${this.curPage}`);
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
