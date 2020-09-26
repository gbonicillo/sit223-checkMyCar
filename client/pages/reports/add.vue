<template>
    <general-contents-container page-title="Add Report">
        <b-form
            @submit.prevent="onSubmit"
        >
            <form-group
                id="make"
                v-model="make"
                label="Make"
                :required="true"
                form-type="select"
                :options="makeOptions"
            />

            <form-group
                id="car"
                v-model="form.car"
                label="Car"
                :required="true"
                form-type="select"
                :options="carOptions"
            />

            <form-group
                id="type"
                v-model="form.type"
                label="Type"
                :required="true"
                form-type="select"
                :options="typeOptions"
            />
            <form-group
                id="title"
                v-model="form.title"
                label="Title"
                :required="true"
                form-type="text"
                placeholder="Enter Title"
            />
            <form-group
                id="description"
                v-model="form.description"
                label="Description (optional)"
                form-type="textarea"
                placeholder="Enter Description"
            />
            <b-button block type="submit" variant="primary">
                Add Report
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
    async asyncData ({ $axios, params }) {
        try {
            const cars = await $axios.$get("/api/cars/choices/1");
            const makes = await $axios.$get("/api/makes/choices");
            return {
                cars,
                makes
            };
        } catch (err) {
            return { cars: [] };
        }
    },
    data () {
        return {
            form: {
                car: 0,
                title: "",
                description: "",
                type: ""
            },
            typeOptions: [
                {
                    value: "IS",
                    text: "Issue"
                },
                {
                    value: "RC",
                    text: "Recall"
                }
            ],
            make: 1,
            cars: [],
            error: null
        };
    },
    computed: {
        carOptions () {
            let options = [];

            this.cars.forEach((car, index) => {
                options.push({
                    value: car.id,
                    text: car.make + ": " + car.model
                });
            });

            options = options.sort((a, b) => {
                return ((a.text < b.text) ? -1 : (a.text > b.text) ? 1 : 0);
            });

            return options;
        },
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
    watch: {
        make (value) {
            this.fetchCars();
        }
    },
    methods: {
        async onSubmit (evt) {
            await this.$axios.post("/api/reports/create", {
                car: this.form.car,
                type: this.form.type,
                title: this.form.title,
                description: this.form.description.length > 0 ? this.form.description
                    : "No description given"
            })
                .then((response) => {
                    if (response.data.id) {
                        this.$router.push({
                            path: `/reports/${response.data.id}`
                        });
                    }
                })
                .catch((err) => {
                    if (err.response.data.title) {
                        this.error = err.response.data.title;
                        $("#title")[0].setCustomValidity(this.error);
                    }
                });
        },
        async fetchCars () {
            try {
                const cars = await this.$axios.$get(`/api/cars/choices/${this.make}`);
                this.cars = cars;
            } catch (err) {
                this.cars = [];
            }
        }
    }
};
</script>

<style lang="scss" scoped>

</style>
