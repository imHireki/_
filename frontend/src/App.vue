<template>
  <div id="wrapper">

    <!-- NAVBAR -->
    <nav class="navbar is-light is-fixed-top" role="navigation" aria-label="main navigation">

      <!-- NAVBAR BRAND -->
      <div class="navbar-brand">
        <!-- BRAND -->
        <router-link to="/" class="navbar-item">
          <span class="icon-text is-medium">
            <span class="icon">
              <i class="fab fa-linux fa-2x"></i>
            </span>
            <span class="is-size-3 ml-2">Yamero</span>
          </span>
        </router-link>
        
        <!-- BURGER -->
        <a role="button" class="navbar-burger" aria-label="menu" aria-expanded="false"
           data-target="navMenu" @click="showMobileMenu = !showMobileMenu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <!-- NAVBAR MENU -->
      <div class="navbar-menu" id="navMenu" v-bind:class="{'is-active': showMobileMenu}">

        <!-- SEARCH -->
        <div class="navbar-item is-expanded">
          <form method="get" action="/search" class="field-body">
            <div class="field has-addons">
              <div class="control is-expanded">
                <input class="input is-rounded" type="text"
                       placeholder="What awesome icons you'd like to see today? 😁"
                       >
              </div>
              <div class="control has-icons-right">
                <button class="button is-rounded">
                <span class="icon"><i class="fa fa-search"></i></span>
                </button>
              </div>
            </div>
          </form>
        </div>

        <!-- DROPDOWN -->
        <div class="navbar-item has-dropdown is-hoverable">
          <a class="navbar-link">Hireki</a>
          <div class="navbar-dropdown is-right">
            <router-link class="navbar-item" to="!#">My Icons</router-link>
            <router-link class="navbar-item" to="!#">Profile</router-link>
            <hr class="navbar-divider">
            <router-link class="navbar-item" to="!#">Settings</router-link>
          </div>
        </div>

      </div>
    </nav>

    <!-- MAIN CONTENT -->
    <section class="section">
      <router-view/>
    </section>

    <!-- FOOTER -->
    <footer class="footer">
      <div class="content has-text-centered">
        <p> &copy; 2021 <strong>Yamero</strong></p>
        <p>Developed with ❤️ by <strong>Hireki</strong></p>
      </div>
    </footer>

  </div>
</template>

<script>
export default {
    data() {
        return {
            showMobileMenu: false,
        }
    }
}
</script>

<style lang="scss">
nav.navbar {
  border-top: 4px solid #276cda;
  margin-bottom: 1rem;
}
</style>
