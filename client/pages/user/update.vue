<template>
    <general-contents-container page-title="Update User Details">
        <b-form
            @submit.prevent="onSubmit"
        >
            <form-group
                id="email"
                v-model="form.email"
                label="Email"
                :placeholder="this.$auth.user.email"
                type="email"
            />
            <b-row>
                <form-group
                    id="firstName"
                    v-model="form.firstName"
                    label="First Name"
                    :placeholder="this.$auth.user.first_name"
                    :value="this.$auth.user.first_name"
                    class="col-lg-6 col-md-12"
                />
                <form-group
                    id="lastName"
                    v-model="form.lastName"
                    label="Last Name"
                    :placeholder="this.$auth.user.last_name"
                    class="col-lg-6 col-md-12"
                />
            </b-row>
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

    middleware: "auth",
    data () {
        return {
            form: {
                email: this.$auth.user.email,
                firstName: this.$auth.user.first_name,
                lastName: this.$auth.user.last_name
            }
        };
    },
    methods: {
        async onSubmit (evt) {
            await this.$axios.put(`/api/auth/user/update/${this.$auth.user.id}`, {
                email: this.form.email,
                first_name: this.form.firstName,
                last_name: this.form.lastName
            })
                .then((response) => {
                    if (response.data.id) {
                        this.$router.push({
                            path: `/user/`
                        });
                    }
                })
                .catch((err) => {
                    if (err.response.data.email) {
                        this.error = err.response.data.email;
                        $("#email")[0].setCustomValidity(this.error);
                    }
                });
        }
    }
};

</script>

<style lang="scss" scoped>

</style>
