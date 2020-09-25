<template>
    <general-contents-container page-title="Update Car">
        <b-form
            @submit.prevent="onSubmit"
        >
            <form-group
                id="make"
                v-model="form.make"
                label="Make"
                :required="true"
                form-type="select"
                :options="makeOptions"
            />

            <form-group
                id="name"
                v-model="form.model"
                label="Model"
                placeholder="Enter model"
                :required="true"
            />
            <b-button block type="submit" variant="primary">
                Update Car
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
            const makes = await $axios.$get("/api/makes/");
            const car = await $axios.$get(`/api/cars/${params.id}/update`);
            return {
                makes,
                form: car
            };
        } catch (err) {
            if (err.response.status === 404) {
                error({ statusCode: 404, message: "Car not found" });
            }

            return { makes: [] };
        }
    },
    data () {
        return {
            form: {
                make: 0,
                model: ""
            },
            makes: [],
            error: null
        };
    },
    computed: {
        makeOptions () {
            const options = [];

            this.makes.forEach((make, index) => {
                options.push({
                    value: make.id,
                    text: make.name
                });
            });

            return options;
        }
    },
    methods: {
        async onSubmit (evt) {
            await this.$axios.put(`/api/cars/${this.form.id}/update`, {
                make: this.form.make,
                model: this.form.model
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
