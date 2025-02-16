<style>
  /* Header and Navigation Styles */
header {
  background-color: #2c3e50;
  padding: 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  color:white;
}

.vertical-nav {
  position: fixed;
  left: 0;
  top:0;
  display: flex;
  flex-direction: column;
  gap: 15px;
  height: 100%;
  width: 180px;
  background-color: #34495e;
  padding: 20px;
  color: white;
  box-shadow: 2px 0 10px rgba(0, 0, 0, 0.1);
  z-index: 100;
}

.nav-item {
  color: #ecf0f1;
  text-decoration: none;
  font-size: 18px;
  padding: 10px 15px;
  border-radius: 4px;
  transition: background-color 0.3s ease;
}

.nav-item:hover {
  background-color: #16a085;
}

.nav-item:active {
  background-color: #1abc9c;
}

/* Content Area */
.content {
  margin-left: 220px;
  width: 100%;
  background-color: #ecf0f1;
  color: #34495e;
}

.layout {
  display: flex;
  flex-direction: row;
  width: 100%;
  height: 100%;
}

/* Mobile Responsiveness */
@media (max-width: 768px) {
  .vertical-nav {
    width: 200px;
  }
}

</style>

<div class="layout">
  <!-- this is to be fixated on the left-->
  <nav class="vertical-nav">

    <a href="/" on:click={() => { localStorage.removeItem('access_token'); goto('/login'); }} class="nav-item">Logout</a>
  </nav>

  <!-- this is to be to the right of it, taking up 100% of height and width -->
  <main class="content">
    <header>

    </header>
      <slot /> <!-- Page content will be injected here -->
  </main>
</div>