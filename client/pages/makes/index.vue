<template>
    <general-contents-container page-title="Makes">
        <template v-slot:header-extra>
            <b-button
                v-if="$auth.user.is_staff"
                variant="primary"
                class="float-lg-right float-sm-left"
                to="/makes/add"
            >
                Add Make
            </b-button>
        </template>
        <b-table
            striped
            hover
            selectable
            responsive
            borderless
            :fields="fields"
            :items="makes"
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
            const result = await $axios.$get("/api/makes/");
            return {
                makes: result.results,
                contentCount: result.count,
                nextPage: result.next,
                prevPage: result.previous
            };
        } catch (err) {
            return { makes: [] };
        }
    },
    data () {
        return {
            fields: ["name"],
            perPage: process.env.paginationItemsPerPage,
            curPage: 1,
            makes: []
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
            const makeId = this.makes[index].id;

            this.$router.push({
                path: `/makes/${makeId}`
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
