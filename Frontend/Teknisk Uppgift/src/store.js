import { createStore } from 'vuex'

const state = {
    authenticated: false,
}

const mutations = {
    setAuthentication(state, status) {
        state.authenticated = status
    },
}

const actions = {

}

export default createStore({state, mutations, actions})