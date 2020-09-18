<template>
    <div>
        <page-header page-title="Add Car" />
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
                Add Car
            </b-button>
        </b-form>
    </div>
</template>

<script>
import PageHeader from "@/components/PageHeader";
import FormGroup from "@/components/FormGroup";

export default {
    components: {
        PageHeader,
        FormGroup
    },
    middleware: ["auth", "is-staff"],
    async asyncData ({ $axios, params }) {
        try {
            const makes = await $axios.$get("/api/makes/");
            return {
                makes
            };
        } catch (err) {
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
            await this.$axios.post("/api/cars/create", {
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
