<template>
    <div>
        <page-header :page-title="'(' + report.type + ') ' + report.car + ': ' + report.title" />
        <p class="text-muted">
            <em>Created: </em> {{ report.created_at }} ||
            <em>Last Updated: </em> {{ report.updated_at }} <br>
        </p>
        <h2>Description</h2>
        <p>
            {{ report.description }}
        </p>
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
            const report = await $axios.$get(`/api/reports/${params.id}`);
            return {
                report
            };
        } catch (err) {
            return {
                report: {
                    id: 0,
                    car: "",
                    title: "",
                    description: "",
                    type: ""
                }
            };
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
        }
    }
};
</script>

<style lang="scss" scoped>

</style>
