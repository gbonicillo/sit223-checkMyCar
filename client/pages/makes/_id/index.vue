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
            :items="cars"
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
    async asyncData ({ $axios, params, error }) {
        try {
            const make = await $axios.$get(`/api/makes/${params.id}`);
            return {
                make,
                cars: make.cars.contents,
                contentCount: make.cars.count
            };
        } catch (err) {
            error({ statusCode: 404, message: "Make not found" });
        }
    },
    data () {
        return {
            fields: ["model"],
            perPage: process.env.paginationItemsPerPage,
            curPage: 1,
            make: {
                id: 0,
                name: ""
            },
            cars: []
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
        },
        async fetchPage () {
            try {
                const result = await this.$axios.$get(`/api/makes/${this.make.id}?page=${this.curPage}`);
                this.cars = result.cars.contents;
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
