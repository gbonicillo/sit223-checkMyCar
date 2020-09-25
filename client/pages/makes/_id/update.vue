<template>
    <general-contents-container page-title="Add Make">
        <b-form
            @submit.prevent="onSubmit"
        >
            <form-group
                id="name"
                v-model="form.name"
                label="Make Name"
                :placeholder="make.name"
            />
            <b-button block type="submit" variant="primary">
                Update
            </b-button>
        </b-form>
    </general-contents-container>
</template>

<script>
import FormGroup from "@/components/FormGroup";
import GeneralContentsContainer from "@/components/GeneralContentsContainer";

export default {
    components: {
        FormGroup,
        GeneralContentsContainer
    },
    middleware: ["auth", "is-staff"],
    async asyncData ({ $axios, params, error }) {
        try {
            const make = await $axios.$get(`/api/makes/${params.id}`);
            return {
                make
            };
        } catch (err) {
            error({ statusCode: 404, message: "Make not found" });
        }
    },
    data () {
        return {
            form: {
                name: ""
            },
            error: null
        };
    },
    methods: {
        async onSubmit (evt) {
            await this.$axios.put(`/api/makes/${this.make.id}/update`, {
                name: this.form.name
            })
                .then((response) => {
                    if (response.data.id) {
                        this.$router.push({
                            path: `/makes/${response.data.id}`
                        });
                    }
                })
                .catch((err) => {
                    if (err.response.data.name) {
                        this.error = err.response.data.name;
                        $("#name")[0].setCustomValidity(this.error);
                    }
                });
        }
    }
};
</script>

<style lang="scss" scoped>

</style>
