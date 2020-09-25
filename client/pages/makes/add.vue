<template>
    <general-contents-container page-title="Add Make">
        <b-form
            @submit.prevent="onSubmit"
        >
            <form-group
                id="name"
                v-model="form.name"
                label="Make Name"
                placeholder="Enter make name"
                :required="true"
            />
            <b-button block type="submit" variant="primary">
                Add Make
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
            await this.$axios.post("/api/makes/create", {
                name: this.form.name
            })
                .then((response) => {
                    if (response.data.id) {
                        this.$router.push({
                            path: `/cars/${response.data.id}`
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
