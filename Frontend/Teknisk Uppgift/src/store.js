import { createStore } from 'vuex'

const state = {
    authenticated: false,
    email: [],
}

const mutations = {
    setAuthentication(state, status) {
        state.authenticated = status
    },
    setEmail(state, status) {
        state.email = status
    }
}

const actions = {

}

export default createStore({state, mutations, actions})