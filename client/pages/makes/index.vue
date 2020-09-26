<template>
    <general-contents-container page-title="Makes">
        <template v-slot:header-extra>
            <b-button
                v-if="$auth.user.is_staff"
                variant="primary"
                class="float-right"
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
            makes: []
        };
    },
    methods: {
        onRowClick (record, index) {
            const makeId = this.makes[index].id;

            this.$router.push({
                path: `/makes/${makeId}`
            });
        }
    }
};
</script>

<style lang="scss" scoped>
</style>
