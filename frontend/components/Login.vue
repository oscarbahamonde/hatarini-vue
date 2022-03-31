<template>
  <div class="hero min-h-screen bg-base-200">
    <div class="hero-content flex-col lg:flex-row-reverse">
      <div class="text-center lg:text-left">
        <h1 class="text-5xl font-bold">Login now!</h1>
        <p class="py-6">
          Provident cupiditate voluptatem et in. Quaerat fugiat ut assumenda excepturi
          exercitationem quasi. In deleniti eaque aut repudiandae et a id nisi.
        </p>
      </div>
      <div class="card flex-shrink-0 w-full max-w-sm shadow-2xl bg-base-100">
        <div class="card-body">
          <div class="form-control">
            <label class="label">
              <span class="label-text">Email</span>
            </label>
            <input
              type="email"
              placeholder="example@email.com"
              class="input input-bordered"
              v-model="email"
            />
          </div>
          <div class="form-control">
            <label class="label">
              <span class="label-text">Password</span>
            </label>
            <input
              type="password"
              placeholder="********"
              class="input input-bordered"
              v-model="password"
            />
            <label class="label">
              <a href="#" class="label-text-alt link link-hover">Forgot password?</a>
            </label>
            <!-- The button to open modal -->
            <label class="btn modal-button" for="my-modal-6">open modal</label>

            <!-- Put this part before </body> tag -->
            <input
              for="my-modal-6"
              type="checkbox"
              id="my-modal-6"
              class="modal-toggle"
            />
            <div class="modal modal-bottom sm:modal-middle">
              <div class="modal-box">
                <h3 class="font-bold text-lg">
                  Put your email, we will send a reset password link
                </h3>
                <p class="py-4">
                  <i class="mdi-email mx-4"></i
                  ><input
                    type="email"
                    placeholder="example@email.com"
                    class="input input-bordered"
                    v-model="email"
                  />
                </p>
                <div class="modal-action">
                  <label for="my-modal-6" class="btn" @click="reset(email)">Reset</label>
                </div>
              </div>
            </div>
          </div>
          <div class="form-control mt-6">
            <button class="btn btn-primary" @click="login(email, password)">Login</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      email: "",
      password: "",
    };
  },
  methods: {
    login(email, password) {
      this.$store.dispatch("LogIn", { email, password });
    },
    reset(email) {
      this.$store.dispatch("Reset", { email });
    },
  },
};
</script>
