<template>
    <general-contents-container :page-title="'(' + report.type + ') ' + report.car + ': ' + report.title">
        <template v-slot:header-extra>
            <add-delete-buttons
                :update-to="`/reports/${report.id}/update`"
                :delete-function="onDeleteClick"
            />
        </template>

        <p class="text-muted">
            <em>Created: </em> {{ report.created_at }} ||
            <em>Last Updated: </em> {{ report.updated_at }} <br>
        </p>
        <h2>Description</h2>
        <p>
            {{ report.description }}
        </p>
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
            const report = await $axios.$get(`/api/reports/${params.id}`);
            return {
                report
            };
        } catch (err) {
            error({ statusCode: 404, message: "Report not found" });
        }
    },
    data () {
        return {
            report: {
                id: 0,
                car: "",
                title: "",
                description: "",
                type: ""
            }
        };
    },
    methods: {
        onRowClick (record, index) {
            const carId = this.car.cars[index].id;

            this.$router.push({
                path: `/cars/${carId}`
            });
        },
        async onDeleteClick (evt) {
            const result = confirm(`Are you sure you want to delete this report?`);
            if (result) {
                await this.$axios.delete(`/api/reports/${this.report.id}`)
                    .then((response) => {
                        this.$router.push({
                            path: "/reports/"
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
