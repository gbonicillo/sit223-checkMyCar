<template>
    <general-contents-container page-title="Cars">
        <template v-slot:header-extra>
            <b-button
                v-if="$auth.user.is_staff"
                variant="primary"
                class="float-lg-right float-sm-left"
                to="/cars/add"
            >
                Add Car
            </b-button>
        </template>
        <b-row>
            <b-input-group>
                <b-form-input
                    v-model="searchTerm"
                    placeholder="Search Cars"
                    @keyup.enter="onSearch"
                />
                <b-input-group-append>
                    <b-button
                        variant="primary"
                        @click="onSearch"
                    >
                        Search
                    </b-button>
                </b-input-group-append>
            </b-input-group>
        </b-row>
        <b-row>
            <b-table
                v-if="cars.length > 0"
                striped
                hover
                selectable
                responsive
                borderless
                :fields="fields"
                :items="cars"
                @row-clicked="onRowClick"
            />
            <h2
                v-else
                class="text-muted"
            >
                <em>There are no cars found using search term "{{ lastSearchTerm }}"</em>
            </h2>
        </b-row>
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
            const result = await $axios.$get("/api/cars/");
            return {
                cars: result.results,
                contentCount: result.count,
                nextPage: result.next,
                prevPage: result.previous
            };
        } catch (err) {
            return { cars: [] };
        }
    },
    data () {
        return {
            fields: [
                {
                    key: "model",
                    sortable: true
                },
                {
                    key: "make",
                    sortable: true
                }
            ],
            perPage: process.env.paginationItemsPerPage,
            curPage: 1,
            cars: [],
            searchTerm: "",
            lastSearchTerm: ""
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
            const carId = this.cars[index].id;

            this.$router.push({
                path: `/cars/${carId}`
            });
        },
        async fetchPage () {
            try {
                const result = await this.$axios.$get(`/api/cars/?page=${this.curPage}`);
                this.cars = result.results;
                this.nextPage = result.next;
                this.prevPage = result.previous;
            } catch (err) {
                this.$toasted.global.defaultError({
                    msg: err
                });
            }
        },
        async onSearch (evt) {
            let searchUrl = "/api/cars/";
            searchUrl = this.searchTerm.length > 0 ? `${searchUrl}?search=${this.searchTerm}` : searchUrl;
            try {
                const result = await this.$axios.$get(searchUrl);
                this.cars = result.results;
                this.next = result.next;
                this.prevPage = result.previous;
                this.contentCount = result.count;

                this.lastSearchTerm = this.searchTerm;
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
