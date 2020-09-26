<template>
    <b-navbar toggleable="md" type="dark" variant="dark">
        <b-navbar-toggle target="nav_collapse" />
        <b-navbar-brand to="/">
            Check Your Car
        </b-navbar-brand>

        <b-navbar-nav
            v-if="this.$auth.loggedIn"
        >
            <b-nav-form>
                <b-form-input
                    v-model="searchTerm"
                    size="sm"
                    class="mr-sm-2"
                    placeholder="Seach Reports"
                />
                <b-button
                    size="sm"
                    class="my-2 my-sm-0"
                    variant="primary"
                    @click="onSearch"
                >
                    Search
                </b-button>
            </b-nav-form>
        </b-navbar-nav>

        <b-collapse id="nav_collapse" is-nav>
            <b-navbar-nav>
                <b-nav-item
                    v-for="(item, key) of this.$auth.loggedIn ? authenticatedItems : globalItems"
                    :key="key"
                    :to="item.to"
                >
                    {{ item.title }}
                </b-nav-item>
            </b-navbar-nav>
            <b-navbar-nav class="ml-auto">
                <b-nav-item-dropdown
                    v-if="this.$auth.loggedIn"
                    :text="this.$auth.user.username"
                    right
                >
                    <b-dropdown-item
                        v-for="(item, key) of rightNavAuthenticatedItems"
                        :key="key"
                    >
                        <b-link :to="item.to">
                            {{ item.title }}
                        </b-link>
                    </b-dropdown-item>
                </b-nav-item-dropdown>
            </b-navbar-nav>
        </b-collapse>
    </b-navbar>
</template>

<script>
export default {
    data () {
        return {
            searchTerm: "",
            globalItems: [
                {
                    title: "Home",
                    to: {
                        name: "index"
                    }
                }
            ],
            authenticatedItems: [
                {
                    title: "Home",
                    to: {
                        name: "index"
                    }
                },
                {
                    title: "Makes",
                    to: {
                        name: "makes"
                    }
                },
                {
                    title: "Cars",
                    to: {
                        name: "cars"
                    }
                },
                {
                    title: "Reports",
                    to: {
                        name: "reports"
                    }
                }
            ],
            rightNavAuthenticatedItems: [
                {
                    title: "Profile",
                    to: {
                        name: "user"
                    }
                },
                {
                    title: "Owned Cars",
                    to: {
                        name: "user-owned-cars",
                        path: "/user/owned-cars"
                    }
                },
                {
                    title: "Update Info",
                    to: {
                        name: "user-update",
                        path: "/user/update"
                    }
                },
                {
                    title: "Change Password",
                    to: {
                        name: "user-change-password",
                        path: "/user/change-password"
                    }
                },
                {
                    title: "Logout",
                    to: {
                        name: "logout"
                    }
                }
            ]
        };
    },
    methods: {
        onSearch (evt) {
            if (this.searchTerm.length > 0) {
                this.$router.push({
                    path: `/reports/?search=${this.searchTerm}`
                });
            } else {
                this.$router.push({
                    path: "/reports/"
                });
            }
        }
    }
};
</script>
