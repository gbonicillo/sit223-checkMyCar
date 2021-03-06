<template>
    <general-contents-container :page-title="car.make + ' ' + car.model">
        <template v-slot:header-extra>
            <add-delete-buttons
                :update-to="`/cars/${car.id}/update`"
                :delete-function="onDeleteClick"
            />
            <b-row align-h="center">
                <b-button
                    v-if="isOwner"
                    variant="danger"
                    @click="onRemoveCarClick"
                >
                    Remove from my Cars
                </b-button>
                <b-button
                    v-else
                    variant="primary"
                    @click="onAddCarClick"
                >
                    Add to my Cars
                </b-button>
            </b-row>
        </template>
        <h2>Reports</h2>
        <b-table
            v-if="reports.length > 0"
            striped
            hover
            selectable
            responsive
            borderless
            :fields="report_fields"
            :items="reports"
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
            const isOwner = await $axios.$get(`/api/cars/${params.id}/owner`);
            return {
                car,
                reports: car.reports.contents,
                contentCount: car.reports.count,
                isOwner: isOwner.is_owner
            };
        } catch (err) {
            error({ statusCode: 404, message: "Car not found" });
        }
    },
    data () {
        return {
            perPage: process.env.paginationItemsPerPage,
            curPage: 1,
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
        },
        async onAddCarClick (evt) {
            const carName = this.car.make + " " + this.car.model;
            const result = confirm(`Add ${carName} to cars you own?`);

            if (result) {
                await this.$axios.put(`/api/cars/${this.car.id}/owner`)
                    .then((response) => {
                        window.location.reload(true);
                    })
                    .catch((err) => {
                        this.$toasted.global.defaultError({
                            msg: err
                        });
                    });
            }
        },
        async onRemoveCarClick (evt) {
            const carName = this.car.make + " " + this.car.model;
            const result = confirm(`Remove ${carName} from cars you own?`);

            if (result) {
                await this.$axios.delete(`/api/cars/${this.car.id}/owner`)
                    .then((response) => {
                        window.location.reload(true);
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
                const result = await this.$axios.$get(`/api/cars/${this.make.id}?page=${this.curPage}`);
                this.reports = result.reports.contents;
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
