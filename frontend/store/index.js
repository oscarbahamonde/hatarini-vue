import { logIn, logOut, getUser, resetPassword } from './auth';

export const state = () => ({
  user: {
    email: 'dev@oscarbahamonde.cloud',
  }
});

export const mutations = {
  setUser(state, user) {
      state.user =  getUser();
  },
  dropUser(state) {
    logOut();
    state.user = null;
  }
};

export const actions = {
  async LogIn({ commit }, { email, password }) {
    const user = await logIn(email, password);
    commit('setUser', user);
  },
  async LogOut({ commit }) {
        commit('dropUser');

  },
  async Reset({ commit }, { email }) {
    await resetPassword(email);
  }
}
