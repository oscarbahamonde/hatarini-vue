<template>
  <div class="drawer">
    <input id="my-drawer-3" type="checkbox" class="drawer-toggle" />
    <div class="drawer-content flex flex-col">
      <div class="w-full navbar bg-neutral text-primary">
        <div class="flex-none lg:hidden">
          <label for="my-drawer-3" class="btn btn-square btn-ghost">
            <i class="mdi-menu"></i>
          </label>
        </div>

        <div class="flex-1">
          <img src="/logo.png" alt="logo" class="w-8 py-2" /><span
            class="text-2xl font-extrabold font-script text-primary"
            >ATARINI</span
          >
        </div>
        <div class="flex-none hidden lg:block">
          <ul class="menu menu-horizontal">
            <li><nuxt-link to="/">Home</nuxt-link></li>
            <li><nuxt-link to="/about">About</nuxt-link></li>
            <li><nuxt-link to="/dashboard">Dashboard</nuxt-link></li>
          </ul>
        </div>
      </div>
      <Nuxt />
    </div>
    <div class="drawer-side">
      <label for="my-drawer-3" class="drawer-overlay"></label>
      <ul class="menu p-4 overflow-y-auto w-60 md:w-80 bg-neutral text-primary">
        <li><nuxt-link to="/">Home</nuxt-link></li>
        <li><nuxt-link to="/about">About</nuxt-link></li>
        <li><nuxt-link to="/dashboard">Dashboard</nuxt-link></li>
      </ul>
    </div>
  </div>
</template>
